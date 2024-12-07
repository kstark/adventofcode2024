import sys
import re

MUL_PATTERN = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')

total = 0
for line in sys.stdin:
    for match in MUL_PATTERN.finditer(line):
        total += int(match[1]) * int(match[2])

print(total)