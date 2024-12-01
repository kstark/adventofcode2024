import sys
from collections import Counter

left, right = [], []
for line in sys.stdin:
    vals = list(map(int, line.split()))
    left.append(vals[0])
    right.append(vals[1])

rcount = Counter(right)
result = 0
for l in left:
    result += l * rcount[l]

print(result)
