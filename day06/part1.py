import sys

DIRECTIONS = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]

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
        grid.append(line)

    return grid, start, obstructions

def iter_steps(grid, start, obstructions):
    y, x = start
    direction_index = 0
    direction = DIRECTIONS[direction_index]
    while x >= 0 and y >= 0 and y < len(grid) and x < len(grid[0]):
        yield y, x
        while (next_step := (y + direction[0], x + direction[1])) in obstructions:
            direction_index = (direction_index + 1) % len(DIRECTIONS)
            direction = DIRECTIONS[direction_index]
        
        y, x = next_step

if __name__ == "__main__":
    grid, start, obstructions = load_file(sys.stdin)
    print(len(set(iter_steps(grid, start, obstructions))))