import sys
from collections import defaultdict
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    y: int
    x: int
    val: int = None

    def __add__(self, other):
        return Point(self.y + other.y, self.x + other.x)
    
    def __str__(self):
        return f"({self.y}, {self.x})={self.val}"

DIRS = (
    Point(-1, 0),
    Point(0, 1),
    Point(1, 0),
    Point(0, -1),
)

VAL_LOW = 0
VAL_HIGH = 9

def in_range(y, x, ylim, xlim):
    return y >= 0 and x >= 0 and y < ylim and x < xlim

def load_file(f) -> list[list[int]]:
    grid = []
    for line in f:
        grid.append(list(map(int, line.strip())))
    return grid

def find_trailhead_score(trailhead: Point, grid):
    seen: defaultdict[Point, int] = defaultdict(lambda: -1)
    ylim, xlim = len(grid), len(grid[0])
    found: set[Point] = set()

    branches = [(trailhead, 0)]
    while branches:
        point, path_length = branches.pop()
        if point.val == VAL_HIGH:
            found.add(point)
            continue
        if path_length <= seen[point]:
            continue
        seen[point] = path_length
        for ndir in DIRS:
            np = point + ndir
            if in_range(np.y, np.x, ylim, xlim) and (nval := grid[np.y][np.x]) == point.val + 1:
                branches.append((Point(np.y, np.x, nval), path_length + 1))
    
    return found

def iter_trailheads(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == VAL_LOW:
                yield Point(y, x, VAL_LOW)

if __name__ == "__main__":
    grid = load_file(sys.stdin)
    total = 0
    for trailhead in iter_trailheads(grid):
        peaks = find_trailhead_score(trailhead, grid)
        print(f"({trailhead.y}, {trailhead.x}): {len(peaks)}")
        total += len(peaks)
    print(total)