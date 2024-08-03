# PythonProjects
# Maze Pathfinding Visualization

This project demonstrates a simple maze pathfinding algorithm using the `curses` library in Python. 
The algorithm performs a breadth-first search (BFS) to find the shortest path from the start point `O` to the end point `X` in a given maze.
# Mastermind Game

A simple Mastermind game implemented in Python. The objective is to guess the correct sequence of colors within a limited number of tries.

## Game Rules

- You have 10 tries to guess the code.
- The code consists of a sequence of 4 colors.
- Valid colors are: `R` (Red), `G` (Green), `B` (Blue), `Y` (Yellow), `W` (White), `O` (Orange).
- After each guess, you'll receive feedback on how many colors are in the correct position and how many are in the incorrect position.

## How to Play

1. Run the game:

```bash
python mastermind.py
Welcome to mastermind, you have 10 tries to guess the code...
The valid colors are:  ['R', 'G', 'B', 'Y', 'W', 'O']

Guess: R G B Y
Correct positions: 2 | Incorrect positions: 1

Guess: W O G B
Correct positions: 1 | Incorrect positions: 2

...
