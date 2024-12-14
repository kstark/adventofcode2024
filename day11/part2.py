import sys
from itertools import islice
from functools import cache

ITER_COUNT = 75

def load_file(f):
    for line in f:
        return [int(stone) for stone in line.strip().split()]
    
@cache
def count_blink(stone, count) -> int:
    if count == 0:
        return 1
    if stone == 0:
        return count_blink(1, count - 1)
    elif (stone_len := len((stone_str := str(stone)))) % 2 == 0:
        l, r = int(stone_str[stone_len // 2:]), int(stone_str[:stone_len // 2])
        return count_blink(l, count - 1) + count_blink(r, count - 1)
    else:
        return count_blink(stone * 2024, count - 1)


if __name__ == "__main__":
    stones = load_file(sys.stdin)
    print(sum(count_blink(s, ITER_COUNT) for s in stones))
