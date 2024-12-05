def read_input(file):
    with open(file) as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].strip() # Removes \n characters from each string
    return lines

def part1(wordsearch):
    xmas_occurences = 0
    for i in range(len(wordsearch)):
        for j in range(len(wordsearch[i])):
            if wordsearch[i][j] == 'X':
                # Search to right
                if j < (len(wordsearch[i]) - 3):
                    if wordsearch[i][j+1] == 'M':
                        if wordsearch[i][j+2] == 'A':
                            if wordsearch[i][j+3] == 'S':
                                xmas_occurences += 1
                # Search to left
                if j > 2:
                    if wordsearch[i][j-1] == 'M':
                        if wordsearch[i][j-2] == 'A':
                            if wordsearch[i][j-3] == 'S':
                                xmas_occurences += 1
                # Search up
                if i > 2:
                    if wordsearch[i-1][j] == 'M':
                        if wordsearch[i-2][j] == 'A':
                            if wordsearch[i-3][j] == 'S':
                                xmas_occurences += 1
                # Search down
                if i < (len(wordsearch) - 3):
                    if wordsearch[i+1][j] == 'M':
                        if wordsearch[i+2][j] == 'A':
                            if wordsearch[i+3][j] == 'S':
                                xmas_occurences += 1
                # Search up-right
                if (i > 2) and (j < (len(wordsearch[i]) - 3)):
                    if wordsearch[i-1][j+1] == 'M':
                        if wordsearch[i-2][j+2] == 'A':
                            if wordsearch[i-3][j+3] == 'S':
                                xmas_occurences += 1
                # Search up-left
                if (i > 2) and (j > 2):
                    if wordsearch[i-1][j-1] == 'M':
                        if wordsearch[i-2][j-2] == 'A':
                            if wordsearch[i-3][j-3] == 'S':
                                xmas_occurences += 1
                # Search down-right
                if (i < (len(wordsearch) - 3)) and (j < (len(wordsearch[i]) - 3)):
                    if wordsearch[i+1][j+1] == 'M':
                        if wordsearch[i+2][j+2] == 'A':
                            if wordsearch[i+3][j+3] == 'S':
                                xmas_occurences += 1
                # Search down-left
                if (i < (len(wordsearch) - 3)) and (j > 2):
                    if wordsearch[i+1][j-1] == 'M':
                        if wordsearch[i+2][j-2] == 'A':
                            if wordsearch[i+3][j-3] == 'S':
                                xmas_occurences += 1
    return xmas_occurences

def part2(wordsearch):
    x_mas_occurences = 0
    valid_x_mas = ['MMASS', 'MSAMS', 'SMASM', 'SSAMM'] # All valid combinations of the X patterns surrounding the 'A'
    for i in range(1, len(wordsearch) - 1):
        for j in range(1, len(wordsearch[i]) - 1):
            if wordsearch[i][j] == 'A':
                x_mas_string = wordsearch[i-1][j-1] + wordsearch[i-1][j+1] + wordsearch[i][j] + wordsearch[i+1][j-1] + wordsearch[i+1][j+1] # Creates string of the X pattern surrounding the 'A'
                if x_mas_string in valid_x_mas:
                    x_mas_occurences += 1
    return x_mas_occurences

def main():
    wordsearch = read_input('day4input.txt')
    part1_ans = part1(wordsearch)
    part2_ans = part2(wordsearch)
    print(part1_ans)
    print(part2_ans)

main()