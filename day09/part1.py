import sys

def load_file(f):
    data = []
    for line in f:
        is_file = True
        file_id = 0
        for chr in line.strip():
            if is_file:
                data.extend(file_id for _ in range(int(chr)))
            else:
                data.extend('.' * int(chr))
            is_file = not is_file
            file_id += int(is_file)

    return data

def compact(data):
    ptr = 0
    fptr = len(data) - 1
    while fptr > ptr:
        if data[ptr] != '.':
            ptr += 1
        elif data[fptr] == '.':
            fptr -= 1
        else:
            data[ptr] = data[fptr]
            data[fptr] = '.'
    return data

def checksum(data):
    return sum(
        i * int(file_id)
        for i, file_id in enumerate(data)
        if file_id != '.'
    )

if __name__ == "__main__":
    data = load_file(sys.stdin)
    compact(data)
    print(checksum(data))