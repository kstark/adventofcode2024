import sys

WORD = 'XMAS'

def flipped(a):
    return [''.join(s[::-1]) for s in a]

def transposed(a):
    return [
        ''.join(a[y][x] for y in range(len(a)))
        for x in range(len(a[0]))
    ]

"""
0,0 0,1 0,2 0,3
1,0 1,1 1,2 1,3
2,0 2,1 2,2 2,3
3,0 3,1 3,2 3,3
"""
def diagonal(a):
    result = []
    startx, starty = 0, 0
    while startx < len(a[0]) and starty < len(a):
        line = []
        x, y = startx, starty
        while x < len(a[0]) and y < len(a) and x >= 0 and y >= 0:
            line.append(a[y][x])
            x += 1
            y -= 1
        result.append(''.join(line))
        if starty < len(a) - 1:
            starty += 1
        else:
            startx += 1
    return result

def load_file(f):
    array = []
    for line in f:
        array.append(line.strip())
    return array

def get_count(array):
    return sum(line.count(WORD) for line in array)

def get_total(array):
    return sum(
        get_count(a)
        for a in [
            array,
            flipped(array),
            transposed(array),
            flipped(transposed(array)),
            diagonal(array),
            flipped(diagonal(array)),
            diagonal(flipped(array)),
            flipped(diagonal(flipped(array))),
        ]
    )

if __name__ == "__main__":
    array = load_file(sys.stdin)
    print(get_total(array))