import sys
import operator

left, right = [], []
for line in sys.stdin:
    vals = list(map(int, line.split()))
    left.append(vals[0])
    right.append(vals[1])

left.sort()
right.sort()
result = 0
for l, r in zip(left, right):
    result += abs(r - l)
print(result)
