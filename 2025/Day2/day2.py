import os

def read_input(file):
    id_ranges = []
    with open(file) as f:
        input = f.readline()
        id_ranges = input.split(',')
    possible_ids = []
    for ranges in id_ranges:
        startend = ranges.split('-')
        startend[0] = int(startend[0])
        startend[1] = int(startend[1])
        for i in range(startend[0], startend[1] + 1):
            possible_ids.append(str(i))
    return possible_ids

def part1(possible_ids):
    # Check every id in list
    total = 0
    for id in possible_ids:
        length = len(id)
        if length % 2 == 0: # Only invalid if same part repeated twice so unable to be invalid on odd length ids
            part1, part2 = id[:length//2], id[length//2:]
            if part1 == part2:
                total += int(id)

    return total

def part2(possible_ids):
    total = 0
    for id in possible_ids:
        length = len(id)
        half = length // 2
        for i in range(1, half + 1):
            chunks = [id[j:j+i] for j in range(0, length, i)]
            if len(set(chunks)) == 1:
                total += int(id)
                break
    return total
           



def main():
    poss_ids = read_input(os.path.join(os.getcwd(), '2025\\Day2\\day2input.txt'))
    part1_ans = part1(poss_ids)
    part2_ans = part2(poss_ids)
    print(part1_ans)
    print(part2_ans)

main()