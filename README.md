# Tic-Tac-Toe using MinMax Algorithm

## Overview
This repository contains code for implementing the MiniMax algorithm and its optimization with alpha-beta pruning for the Tic-Tac-Toe game. This project focuses on two key aspects of adversarial search:

1. **MiniMax Search:** The core algorithm that explores all possible game states to identify the move that maximizes the score for the player (Max).
2. **Alpha-Beta Pruning:** An optimization technique that reduces the search space in the MiniMax algorithm, leading to faster execution, especially for larger game boards.

## Breakdown

### Part 1: MiniMax Search
* **Evaluation Function:** Defined within `MinMax_algorithm.py`, it evaluates the current game state from Max's perspective, returning:
    * `1`: Max has won (favorable for Max)
    * `-1`: Min (opponent) has won (unfavorable for Max)
    * `0`: Draw or insufficient information to judge.
* **Finding the Best Path for Max:** MiniMax recursively traverses the game tree, analyzing potential moves, and returning the path that maximizes Max's score.

### Part 2: Search Space Reduction with Alpha-Beta Pruning
* **Optimization:** The `MiniMax_with_Alpha-Beta_Pruning.py` script implements MiniMax with alpha-beta pruning.
* **Pruning Mechanism:** This technique eliminates branches in the game tree that cannot affect the optimal decision for Max, based on the current alpha and beta values. These values represent the highest score Max can guarantee and the lowest score Min can force, respectively.
* **Improved Efficiency:** By pruning irrelevant branches, the search space is reduced, leading to faster execution, particularly for larger game boards or more complex games.

## Requirements
- **Programming Language:** Python
- **Development Environment:** VS Code, Google Colab, Jupyter Notebook

## Mentor
My sincere gratitude to **Dr. Soharab Hossain Shaikh** for his guidance and mentorship throughout the development of this task.

## Purpose
The purpose is to explore and implement the MiniMax algorithm and its optimization through alpha-beta pruning, demonstrating how these techniques can efficiently solve decision-making problems in adversarial games like Tic-Tac-Toe.

## Key Features
- Comprehensive implementation of MiniMax search for optimal decision-making.
- Alpha-beta pruning to optimize the search process, making it faster and more efficient.
- Detailed evaluation function to assess game states from Max's perspective.

## Explore the Code
Feel free to explore the codebase, try different strategies, and understand how the MiniMax algorithm is applied in game scenarios:
* **Part 1 (MiniMax Search):** [MiniMax Search Code](https://onlinegdb.com/ZqGu-G4EMx)
* **Part 2 (Alpha-Beta Pruning with MiniMax):** [Alpha-Beta Pruning Code](https://onlinegdb.com/H-jk1Wl1z)

## Contact
For inquiries, collaboration opportunities, or further information, please feel free to reach out to:

Email: nikhilgodavarthi9@gmail.com

Thank you for exploring this project and learning about the efficient implementation of the MiniMax algorithm with alpha-beta pruning!
