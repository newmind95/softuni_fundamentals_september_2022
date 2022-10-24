from typing import List, Tuple


rows = int(input())


def read_maze() -> List[List[str]]:
    maze = []
    for row in range(rows):
        line = list(input())
        maze.append(line)

    return maze


def is_valid_cell(row: int, col: int, maze: List[List[str]]) -> bool:
    return (0 <= row < len(maze)) and (0 <= col < len(maze))


def find_position_of_Kate(maze: List[List[str]]) -> Tuple[int]:
    kate_row, kate_col = 0, 0
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == 'k':
                return row, col


def get_directions() -> List[Tuple[int]]:
    return [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0)
    ]


def count_paths_to_exit(maze: List[List[str]]) -> int:
    kate_row, kate_col = find_position_of_Kate(maze)
    longest_moves = 0
    rows_count = len(maze)
    cols_count = len(maze[0])
    directions = get_directions()
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            print(maze[row-1][col], end='') 
        print()


maze = read_maze()
print(count_paths_to_exit(maze))
