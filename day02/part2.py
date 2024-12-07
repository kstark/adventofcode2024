import sys
from itertools import pairwise

def is_safe(nums, recurse=1):
    if recurse < 0:
        return False
    
    direction = None
    for i, (l, r) in enumerate(pairwise(nums)):
        diff = abs(r - l)
        new_direction = r > l
        if diff == 0 or diff > 3:
            return (
                is_safe(nums[:i - 1] + nums[i:], recurse - 1)
                or is_safe(nums[:i] + nums[i + 1:], recurse - 1)
                or is_safe(nums[:i + 1] + nums[i + 2:], recurse - 1)
            )
        elif direction is None:
            direction = new_direction
        elif new_direction != direction:
            return (
                is_safe(nums[:i - 1] + nums[i:], recurse - 1)
                or is_safe(nums[:i] + nums[i + 1:], recurse - 1)
                or is_safe(nums[:i + 1] + nums[i + 2:], recurse - 1)
            )
        
    return True

def _is_safe(nums):
    return (
        len(nums) == len(set(nums)) and
        (all(nums[i] < nums[i + 1] for i in range(len(nums) - 1)) or
         all(nums[i] > nums[i + 1] for i in range(len(nums) - 1))) and
        all(abs(nums[i] - nums[i + 1]) <= 3 for i in range(len(nums) - 1))
    )

def is_safe_manual(nums):
    if _is_safe(nums):
        return True
    for i in range(len(nums)):
        new_nums = list(nums)
        new_nums.pop(i)
        result = _is_safe(new_nums)
        print(f' {int(result)}: {new_nums}')
        if result:
            return True
    return False

safe_count = 0
for line in sys.stdin:
    nums = list(map(int, line.split()))
    result = is_safe(nums)
    print(f'{int(result)}: {line.strip()}')
    safe_count += result

print(safe_count)