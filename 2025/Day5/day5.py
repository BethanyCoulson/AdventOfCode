import os

def read_input(file):
    ids = []
    ranges = []
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            if line != '\n':
                if '-' in line:
                    line = line.rstrip()
                    range_start, range_end = map(int, line.split('-'))
                    ranges.append((range_start, range_end))
                else:
                    ids.append(int(line.rstrip()))

    return ranges, ids  

def part1(fresh_IDs, IDs):
    total = 0
    for ID in IDs:
        if any(start <= ID <= end for start, end in fresh_IDs):
            total += 1

    return total

def part2(ranges):
    total = 0
    ranges.sort()
    merged = []

    for start, end in ranges:
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    for start, end in merged:
        total += end - start + 1

    return total


def main():
    fresh_IDS, IDs = read_input(os.path.join(os.getcwd(), '2025\\Day5\\day5input.txt'))
    part1_ans = part1(fresh_IDS, IDs)
    part2_ans = part2(fresh_IDS)
    print(part1_ans)
    print(part2_ans)

main()