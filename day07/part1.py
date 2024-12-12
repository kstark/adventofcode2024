import sys
import operator
import itertools

OPERATORS = {
    '+': operator.add,
    '*': operator.mul,
}

def load_file(f):
    results = []
    for line in f:
        total, rest = line.split(': ')
        results.append((int(total), [int(n) for n in rest.split()]))
    return results

def _find_total(goal, numbers, accum, ops):
    if not numbers:
        return goal == accum, ops
    if accum > goal and numbers:
        return False, ops
    
    for op, opfunc in OPERATORS.items():
        taccum = opfunc(accum, numbers[0])
        result, all_ops = _find_total(goal, numbers[1:], taccum, ops + [op])
        if result:
            return result, all_ops
        
    return False, ops

def find_total(goal, numbers):
    result, ops = _find_total(goal, numbers[1:], numbers[0], [])
    if result:
        opstring = " ".join(str(x) for x in itertools.chain.from_iterable(itertools.zip_longest(numbers, ops, fillvalue=None)) if x is not None)
        print(f'{goal}: {result} {opstring}')
    else:
        print(f'{goal}: {result} {" ".join(str(n) for n in numbers)}')
    return result

if __name__ == "__main__":
    data = load_file(sys.stdin)
    total = 0
    for goal, numbers in data:
        result = find_total(goal, numbers)
        if result:
            total += goal
    print(total)