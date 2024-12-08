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

def get_ordered(section, ordering: list):
    return sorted(section, key=ordering.index)

def topo_sort_kahns(input_constraints):
    """
    Kahn's algorithm

    Had cycle issues, not sure why
    """
    constraints = defaultdict(set)
    for parent, prefixes in input_constraints.items():
        constraints[parent].update(prefixes)
    rev_constraints = defaultdict(set)
    for parent, prefixes in constraints.items():
        for node in prefixes:
            rev_constraints[node].add(parent)

    result = []
    S = {node for node in rev_constraints if node not in constraints}
    while S:
        result.append(node := S.pop())
        dependencies = list(rev_constraints[node])
        for dependency in dependencies:
            rev_constraints[node].remove(dependency)
            constraints[dependency].remove(node)
            if not constraints[dependency]:
                S.add(dependency)
    
    if sum(len(prefixes) for prefixes in constraints.values()) > 0:
        raise Exception("cycle")
    return result

def topo_sort_dfs(input_constraints):
    result = []
    all_nodes = set(input_constraints.keys()) | {n for v in input_constraints.values() for n in v}
    pmarked = set()
    tmarked = set()

    def visit(node):
        if node in pmarked:
            return
        if node in tmarked:
            raise Exception("cycle")
        
        tmarked.add(node)
        for m in input_constraints[node]:
            visit(m)
        
        pmarked.add(node)
        result.append(node)

    while pmarked < all_nodes:
        visit((all_nodes - pmarked).pop())
    return result

def iter_middles(constraints, sections):
    for section in sections:
        if not is_ordered(section, constraints):
            # Limit to only relevant rules
            limited_constraints = {
                k: {node for node in v if node in section}
                for k, v in constraints.items() if k in section
            }
            ordering = topo_sort_dfs(limited_constraints)
            section = get_ordered(section, ordering)
            yield section[len(section) // 2]


if __name__ == "__main__":
    total = 0
    constraints, sections = load_file(sys.stdin)
    for middle in iter_middles(constraints, sections):
        total += int(middle)
    print(total)