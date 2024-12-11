import sys
from collections import defaultdict
from itertools import islice

DIRECTIONS = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]

def turn(direction_index):
    return (direction_index + 1) % len(DIRECTIONS)

def load_file(f):
    grid = []
    start = None
    obstructions = set()
    for y, line in enumerate(l.strip() for l in f):
        for x, c in enumerate(line):
            match c:
                case '#':
                    obstructions.add((y, x))
                case '^':
                    start = (y, x)
        grid.append(list(line))

    return grid, start, obstructions

def iter_steps(grid, start, obstructions, direction_index=0):
    y, x = start
    direction = DIRECTIONS[direction_index]
    while x >= 0 and y >= 0 and y < len(grid) and x < len(grid[0]):
        is_corner = False
        while (next_step := (y + direction[0], x + direction[1])) in obstructions:
            is_corner = True
            direction_index = turn(direction_index)
            direction = DIRECTIONS[direction_index]

        yield y, x, is_corner, direction_index
        y, x = next_step


def get_new_obstacles(grid, start, obstructions):

    # y, x = start
    # direction_index = 0
    # direction = DIRECTIONS[direction_index]
    visited = defaultdict(set)
    corners = dict()
    new_obstacles = set()
    for y, x, is_corner, direction_index in iter_steps(grid, start, obstructions):
        if direction_index in visited[(y, x)]:
            break
        visited[(y, x)].add(direction_index)
        match grid[y][x], is_corner, direction_index:
            case '^', _:
                pass
            case _, True, _:
                grid[y][x] = '+'
            case '.', _, 0 | 2:
                grid[y][x] = '|'
            case '.', _, 1 | 3:
                grid[y][x] = '-'
            case '-', _, 0 | 2:
                grid[y][x] = '+'
            case '|', _, 1 | 3:
                grid[y][x] = '+'
        if is_corner:
            corners[(y, x)] = 1

        try:
            # Get potential new obstacle - can't intersect somewhere we've already visited
            ny, nx, _, ndi = next(islice(iter_steps(grid, (y, x), obstructions, direction_index), 1, None))
            if (ny, nx) in visited:
                continue
        except StopIteration:
            continue

        test_direction_index = turn(direction_index)
        test_obstructions = set(obstructions) | {(ny, nx)}
        test_visited = defaultdict(set)
        for point, directions in visited.items():
            test_visited[point].update(directions)

        for ty, tx, _, tdi in iter_steps(grid, (y, x), test_obstructions, test_direction_index):
            if tdi in test_visited[(ty, tx)]:
                # print(f'From {(x, y)}, repeat corner {(ty, tx, tdi)}, yield {(ny, nx)}')
                new_obstacles.add((ny, nx))
                break
            test_visited[(ty, tx)].add(tdi)
    return visited, new_obstacles


if __name__ == "__main__":
    grid, start, obstructions = load_file(sys.stdin)
    visited, new_obstacles = get_new_obstacles(grid, start, obstructions)
    for y, x in new_obstacles:
        grid[y][x] = 'O'
    for row in grid:
        print(''.join(row))
    print(len(visited))
    print(len(new_obstacles))
