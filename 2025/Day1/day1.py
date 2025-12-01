import os

def read_input(file):
    instructions = []
    with open(file) as f:
        lines = f.readlines() # Splits lines into array
        for line in lines:
            instructions.append(line)
    return instructions

def calculate_new_position(c_pos, ins):
    

    return c_pos 

def part1(instructions):
    count = 0
    current_pos = 50
    for i in range(0, len(instructions)):
        instr = instructions[i]
        direction = instr[0]
        number = int(instr[1:].split('\n')[0]) # Removes the newline from the number aspect of password and turns to int
        if direction == "L":
            number *= -1
        current_pos = (current_pos + number) % 100
        if current_pos == 0:
            count += 1
    return count

def part2(instructions):
    count = 0
    current_pos = 50
    for i in range(0, len(instructions)):
        instr = instructions[i]
        direction = instr[0]
        number = int(instr[1:].split('\n')[0]) # Removes the newline from the number aspect of password and turns to int
        count += number // 100 # Number of full wraps
        if direction == "L": 
            number *= -1
        new_pos = (current_pos + number) % 100
        if current_pos != 0 and new_pos != 0: # Doesn't recount if landing on a 0
            if (number < 0 and new_pos > current_pos) or (number > 0 and new_pos < current_pos):
                count += 1 # Checks for extra wrap over the multiples of 100
        if new_pos == 0:
            count += 1
        current_pos = new_pos 
    return count



def main():
    instructions = read_input(os.path.join(os.getcwd(), '2025\\Day1\\day1input.txt'))
    part1_ans = part1(instructions)
    part2_ans = part2(instructions)
    print(part1_ans)
    print(part2_ans)

main()