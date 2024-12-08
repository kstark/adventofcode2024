import sys
from collections import defaultdict



def load_file(f):
    constraints = defaultdict(set)
    sections = []
    for line in f:
        if '|' in line:
            before, after = line.strip().split('|')
            constraints[after].add(before)
        elif ',' in line:
            sections.append(line.strip().split(','))

    return constraints, sections

def is_ordered(section, constraints):
    found = set()
    valid = set(section)
    for page in section:
        if not (constraints[page] & valid) <= found:
            return False
        found.add(page)
    return True

def iter_middles(constraints, sections):
    for section in sections:
        if is_ordered(section, constraints):
            yield section[len(section) // 2]


if __name__ == "__main__":
    total = 0
    constraints, sections = load_file(sys.stdin)
    for middle in iter_middles(constraints, sections):
        total += int(middle)
    print(total)