import sys
from itertools import islice

ITER_COUNT = 25

def load_file(f):
    for line in f:
        return [int(stone) for stone in line.strip().split()]
    
def iter_stones(stones):
    while True:
        stones = list(stones)
        for i in range(len(stones) - 1, -1, -1):
            if stones[i] == 0:
                stones[i] = 1
            elif (stone_len := len((stone_str := str(stones[i])))) % 2 == 0:
                stones[i] = int(stone_str[stone_len // 2:])
                stones.insert(i, int(stone_str[:stone_len // 2]))
            else:
                stones[i] *= 2024
        yield stones

if __name__ == "__main__":
    stones = load_file(sys.stdin)
    after = next(islice(iter_stones(stones), ITER_COUNT - 1, None))

    print(len(after))