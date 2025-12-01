def read_input(file):
    page_dict = {}
    updates = []
    with open(file) as f:
        contents = f.readlines()
        for line in contents:
            line = line.strip()
            if '|' in line:
                page1, page2 = line.split('|')
                page1, page2 = int(page1), int(page2)
                if not (page1 in page_dict.keys()):
                    page_dict[page1] = [page2]
                else:
                    page_dict[page1].append(page2)
            if ',' in line:
                updates.append(line)
    return page_dict, updates

def part1(rules, updates):
    total = 0
    for update in updates:
        pass

def main():
    rules, updates = read_input("day5input.txt")
    part1_ans = part1(rules, updates)

#main()

from itertools import count

with open('day5input.txt', 'r') as file:
    input = file.read().split('\n')

empty_line_index = next(i for i, j in zip(count(), input) if j == "")

updates = input[empty_line_index + 1:]

ordering_rules = []

for line in input[:empty_line_index]:
    line = line.split('|')
    ordering_rules.append(line[0] + line[1])


# FUNCTIONS

def sorted_checker(data: list):
    if all(data[i] + data[i+1] in ordering_rules for i in range(len(data) - 1)):
        return True
    
    return False


# PARTS 1 & 2

result1 = 0
result2 = 0

for update in updates:
    if not update:
        continue

    update = update.split(',')

    middle_index = (len(update) - 1) // 2

    if sorted_checker(update):
        result1 += int(update[middle_index])
        continue

    sorted = False

    while sorted == False:
        for i in range(len(update) - 1):
            if update[i] + update[i+1] not in ordering_rules:
                update[i], update[i+1] = update[i+1], update[i]
        if sorted_checker(update):
            sorted = True
    
    result2 += int(update[middle_index])


print("Part 1 answer: ", result1)
print("Part 2 answer: ", result2)