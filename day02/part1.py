import sys
from itertools import pairwise

def is_safe(nums):
    direction = None
    for l, r in pairwise(nums):
        diff = abs(r - l)
        new_direction = r > l
        if diff == 0 or diff > 3:
            return False
        elif direction is None:
            direction = new_direction
        elif new_direction != direction:
            return False
        
    return True

safe_count = 0
for line in sys.stdin:
    nums = list(map(int, line.split()))
    safe_count += is_safe(nums)

print(safe_count)