class TicTacToe:
    def __init__(self, player_choice, agent_choice):
        self.board = [' ' for _ in range(9)]
        self.player_choice = player_choice
        self.agent_choice = agent_choice

    def display_board(self):
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("---|---|---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("---|---|---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")

    def is_full(self):
        return ' ' not in self.board

    def is_winner(self, player):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]

        for condition in win_conditions:
            if all(self.board[i] == player for i in condition):
                return True
        return False

    def make_move(self, move, player):
        if self.board[move] == ' ':
            self.board[move] = player
            return True
        return False

    def undo_move(self, move):
        self.board[move] = ' '

    def evaluate_board(self, player, agent):
        if self.is_winner(player):
            return 1
        elif self.is_winner(agent):
            return -1
        elif self.is_full():
            return 0
        else:
            return 0

def welcome_message():
    print("Welcome to Tic-Tac-Toe! You can choose to play as 'X' or 'O'.")
    user_choice = input("Select 'X' or 'O': ").upper()
    while user_choice not in ['X', 'O']:
        print("Invalid choice. Please select 'X' or 'O'.")
        user_choice = input("Select 'X' or 'O': ").upper()
    if user_choice == 'X':
        agent_choice = 'O'
    else:
        agent_choice = 'X' 
    print(f"You chose {user_choice}. You will play first.")
    print(f"The Agent will play as {agent_choice}.")
    return user_choice, agent_choice

def get_player_move():
    while True:
        try:
            move = int(input("Enter your move (0-8): "))
            if move < 0 or move > 8:
                print("Invalid move. Please enter a number between 0 and 8.")
                continue
            return move
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 8.")

def main():
    player_choice, agent_choice = welcome_message()
    if player_choice == 'O':
        current_player = 'X'
    else:
        current_player = player_choice

    game = TicTacToe(player_choice, agent_choice)

    while not game.is_full() and not game.is_winner(player_choice) and not game.is_winner(agent_choice):
        game.display_board()

        if current_player == player_choice:
            player_move = get_player_move()
            if game.make_move(player_move, player_choice):
                current_player = agent_choice
            else:
                print("Invalid move. Try again.")
                continue
        else:
            best_move = find_best_move(game, agent_choice, player_choice) 
            print(f"Agent's move: {best_move}")
            game.make_move(best_move, agent_choice)
            current_player = player_choice

        if game.is_winner(player_choice):
            game.display_board()
            print("You win!")
            break
        elif game.is_winner(agent_choice):
            game.display_board()
            print("Agent wins!")
            break
        elif game.is_full():
            game.display_board()
            print("It's a draw!")
            break

def find_best_move(board, agent_choice, player_choice):
    best_move = -1
    best_eval = -float('inf')

    for move in range(9):
        if board.board[move] == ' ':
            board.make_move(move, agent_choice)
            eval = minimax(board, 0, False, agent_choice, player_choice, agent_choice)
            board.undo_move(move)
            if eval > best_eval:
                best_eval = eval
                best_move = move
    return best_move

    
def minimax(board, depth, is_maximizing, current_player, player, agent):
    if board.is_winner(player):
        return -1
    if board.is_winner(agent): 
        return 1
    if board.is_full():
        return 0

    if is_maximizing:
        max_eval = -float('inf')
        for move in range(9):
            if board.board[move] == ' ':
                board.make_move(move, current_player)
                eval = minimax(board, depth + 1, False, current_player, player, agent)
                board.undo_move(move)
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in range(9):
            if board.board[move] == ' ':
                board.make_move(move, player if current_player == agent else agent)
                eval = minimax(board, depth + 1, True, current_player, player, agent)
                board.undo_move(move)
                min_eval = min(min_eval, eval)
        return min_eval
   
if __name__ == "__main__":
    player_choice, agent_choice = 'X', 'O'
    game = TicTacToe(player_choice, agent_choice)
    current_player = player_choice
    main()
