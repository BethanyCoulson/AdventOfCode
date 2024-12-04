import re

def read_input(file):
    with open(file) as f:
        contents = f.read()
    return contents

def part1(corrupt_memory):
    sum_muls = 0
    valid_muls = re.findall(r'mul\(\d{1}\d?\d?,\d{1}\d?\d?\)', corrupt_memory) # Finds all valid multiply funcs in the corrupt memory and stores in list
    for mul in valid_muls:
        nums = list(map(int, re.sub("[mul()]", "", mul).split(","))) # Takes 2 numbers from the mul function and stores in list
        sum_muls += nums[0]*nums[1] # Multiplies two numbers and adds to total
    return sum_muls 

def part2(corrupt_memory):
    sum_muls = 0
    do_segments = corrupt_memory.split("do()") # Split at do() functions 
    for seg in do_segments: # Checks each segment
        dont_removed = seg.split("don't()")[0] # Removes the segment of the string after dont() function
        valid_muls = re.findall(r'mul\(\d{1}\d?\d?,\d{1}\d?\d?\)', dont_removed) # Finds all valid multiply funcs that occur before the dont()
        for mul in valid_muls:
            nums = list(map(int, re.sub("[mul()]", "", mul).split(","))) # Takes 2 numbers from the mul function and stores in list
            sum_muls += nums[0]*nums[1] # Multiplies two numbers and adds to total
    return sum_muls

def main():
    corrupt_memory = read_input('day3input.txt')
    part1_ans = part1(corrupt_memory)
    part2_ans = part2(corrupt_memory)
    print(part1_ans)
    print(part2_ans)

main()