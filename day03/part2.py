import sys
import re

MUL_PATTERN = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
SWITCH_PATTERN = re.compile(r"(do|don't)\(\)")

total = 0
enabled = True
for line in sys.stdin:
    for part in SWITCH_PATTERN.split(line):
        if part == "do":
            enabled = True
        elif part == "don't":
            enabled = False
        else:
            for match in MUL_PATTERN.finditer(part):
                if enabled:
                    total += int(match[1]) * int(match[2])

print(total)