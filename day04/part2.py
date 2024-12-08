import sys

all_found = set()
def load_file(f):
    array = []
    for line in f:
        # print(line.strip())
        array.append(line.strip())
    return array

def match(array, x, y):
    if array[y][x] != 'A':
        return False
    if 0 in (x, y) or x == len(array[0]) - 1 or y == len(array) - 1:
        return False
    test = ''.join([
        array[y - 1][x - 1],
        array[y + 1][x + 1],
        array[y + 1][x - 1],
        array[y - 1][x + 1],
    ])
    result = sorted(test[:2]) + sorted(test[2:]) == list('MSMS')
    # if result and x == 0 or y == 0:
    #     print(f'{x},{y}: {test}')
    #     print(f'{array[y-1][x-1:x+2]}\n{array[y][x-1:x+2]}\n{array[y+1][x-1:x+2]}')
    #     p = f'{test[0]}.{test[3]}\n.A.\n{test[2]}.{test[1]}'
    #     all_found.add(p)
    #     print(p)
    return result
    
def get_match_count(array):
    return sum(
        match(array, x, y)
        for y in range(len(array))
        for x in range(len(array[0]))
    )

if __name__ == "__main__":
    array = load_file(sys.stdin)
    print(get_match_count(array))
    list(map(print, all_found))