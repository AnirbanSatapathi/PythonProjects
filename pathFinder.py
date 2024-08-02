import curses
from curses import wrapper
import queue
import time

maze = [
    ["#", " ", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", "O", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "X", "#", "#", "#", "#", "#"]
]

def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j*2, "X", BLUE)
            else:
                stdscr.addstr(i, j*2, value, RED)

def begin(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j
    return None

def find_path(maze, stdscr):
    start = "O"
    end = "X"
    start_pos = begin(maze, start)
    q = queue.Queue()
    q.put((start_pos, [start_pos]))
    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.2)
        stdscr.refresh()

        if maze[row][col] == end:
            return path

        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue
            r, c = neighbor
            if maze[r][c] == "#":
                continue

            new_path = path + [neighbor]
            q.put((neighbor, new_path))
            visited.add(neighbor)

def find_neighbors(maze, row, col):
    neighbors = []
    if row > 0:
        neighbors.append((row-1, col)) # up
    if row < len(maze) - 1:
        neighbors.append((row+1, col)) # down
    if col > 0:
        neighbors.append((row, col-1)) # left
    if col < len(maze[0]) - 1:
        neighbors.append((row, col+1)) # right
    return neighbors

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    find_path(maze, stdscr)
    stdscr.getch()

wrapper(main)