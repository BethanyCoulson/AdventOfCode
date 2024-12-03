def read_input(file):
    first_list = []
    second_list = []
    with open(file) as f:
        lines = f.readlines() # Splits lines into array
        for line in lines:
            lineval = line.split() # Splits each line into the 2 IDs
            first_list.append(int(lineval[0])) # Adds corresponding ID to first list as an integer
            second_list.append(int(lineval[1])) # Adds corresponding ID to second list as an integer
    return first_list, second_list

def part1(location_id1, location_id2):
    total_dist_diff = 0 # Tracks the total difference in distances for the two location ID lists
    location_id1.sort() # Sorts into ascending order
    location_id2.sort() # Sorts into ascending order
    for i in range(len(location_id1)):
        total_dist_diff += abs(location_id1[i] - location_id2[i])
    return total_dist_diff

def part2(location_id1, location_id2):
    total_sim_score = 0 # Tracks the total similarity score
    for id in location_id1:
        num_match = 0 # Tracks number of ids in location_id2 that match id
        for id2 in location_id2:
            if id2 == id:
                num_match += 1
        total_sim_score += (id*num_match)
    return total_sim_score

def main():
    location_id1, location_id2 = read_input('day1input.txt')
    part1_ans = part1(location_id1, location_id2)
    part2_ans = part2(location_id1, location_id2)
    print(part1_ans)
    print(part2_ans)

main()