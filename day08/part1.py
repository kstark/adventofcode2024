import sys
from collections import defaultdict
from itertools import combinations

def load_file(f: list[list[str]]):
    grid = []
    locs = defaultdict(list)
    for y, line in enumerate(f):
        for x, chr in enumerate(line):
            if chr.isalnum():
                locs[chr].append((y, x))
        grid.append(list(line.strip()))
    return grid, locs

def calc_antinodes(l, r):
    ydiff, xdiff = l[0] - r[0], l[1] - r[1]
    return (
        (l[0] + ydiff, l[1] + xdiff),
        (r[0] - ydiff, r[1] - xdiff),
    )

def get_antinodes(grid, locs):
    ymax, xmax = len(grid), len(grid[0])
    antinodes = set()
    for chr, nodes in locs.items():
        for l, r in combinations(nodes, 2):
            for ay, ax in calc_antinodes(l, r):
                if ax < 0 or ay < 0 or ax >= xmax or ay >= ymax:
                    continue
                antinodes.add((ay, ax))
                if grid[ay][ax] == '.':
                    grid[ay][ax] = '#'
    return antinodes

if __name__ == "__main__":
    grid, locs = load_file(sys.stdin)
    antinodes = get_antinodes(grid, locs)
    for line in grid:
        print(''.join(line))

    print(len(antinodes))