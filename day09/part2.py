import sys
from dataclasses import dataclass

@dataclass
class run:
    length: int
    id: int | None = None

    def __str__(self) -> str:
        return str('.' if self.id is None else self.id) * self.length


def load_file(f):
    data = []
    for line in f:
        is_file = True
        file_id = 0
        for chr in line.strip():
            if is_file:
                data.append(run(length=int(chr), id=file_id))
            else:
                data.append(run(length=int(chr)))
            is_file = not is_file
            file_id += int(is_file)

    return data

def compact(data: list[run]):
    seek_id = None
    fptr = len(data) - 1
    # print(''.join(str(r) for r in data))
    while fptr > 0:
        if data[fptr].id is None:
            fptr -= 1
            continue
        if seek_id is None:
            seek_id = data[fptr].id
        if (source := data[fptr]).id == seek_id:
            sptr = 0
            seek_id -= 1
            while sptr < fptr:
                dest = data[sptr]
                if dest.id is None and dest.length > source.length:
                    data[sptr] = run(dest.length - source.length)
                    data[fptr] = run(source.length)
                    data.insert(sptr, source)
                    fptr += 1
                    # print(''.join(str(r) for r in data))
                    break
                elif dest.id is None and dest.length == source.length:
                    data[sptr] = source
                    data[fptr] = dest
                    # print(''.join(str(r) for r in data))
                    break
                sptr += 1
        fptr -= 1
    return data

def spread(data):
    for r in data:
        for _ in range(r.length):
            yield r.id

def checksum(data: list[run]):
    return sum(
        i * file_id
        for i, file_id in enumerate(spread(data))
        if file_id is not None
    )

if __name__ == "__main__":
    data = load_file(sys.stdin)
    compact(data)
    print(checksum(data))