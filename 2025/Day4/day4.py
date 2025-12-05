import os

def read_input(file):
    paper_grid = []
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            paper_grid.append(line.rstrip())
    return paper_grid

def part1(grid):
    rows = len(grid)
    columns = len(grid[0])
    total = 0
    for i in range(rows):
        for j in range(columns):
            rolls_adjacent = 0
            if grid[i][j] == '@':
                # Check up-left
                if i > 0 and j > 0:
                    if grid[i-1][j-1] == '@':
                        rolls_adjacent += 1
        
                # Check up-mid
                if i > 0:
                    if grid[i-1][j] == '@':
                        rolls_adjacent += 1

                # Check up-right
                if i > 0 and j < columns - 1:
                    if grid[i-1][j+1] == '@':
                        rolls_adjacent += 1

                # Check left
                if j > 0:
                    if grid[i][j-1] == '@':
                        rolls_adjacent += 1

                # Check right
                if j < columns - 1:
                    if grid[i][j+1] == '@':
                        rolls_adjacent += 1

                # Check down-left
                if i < rows - 1 and j > 0:
                    if grid[i+1][j-1] == '@':
                        rolls_adjacent += 1

                # Check down-mid
                if i < rows - 1:
                    if grid[i+1][j] == '@':
                        rolls_adjacent += 1

                # Check down-right
                if i < rows - 1 and j < columns - 1:
                    if grid[i+1][j+1] == '@':
                        rolls_adjacent += 1

                if rolls_adjacent < 4:
                    total += 1

    return total

def part2(grid):
    rows = len(grid)
    columns = len(grid[0])
    total = 0
    continue_removal = True
    while continue_removal:
        indexes_to_remove = []
        for i in range(rows):
            for j in range(columns):
                rolls_adjacent = 0
                if grid[i][j] == '@':
                    # Check up-left
                    if i > 0 and j > 0:
                        if grid[i-1][j-1] == '@':
                            rolls_adjacent += 1
            
                    # Check up-mid
                    if i > 0:
                        if grid[i-1][j] == '@':
                            rolls_adjacent += 1

                    # Check up-right
                    if i > 0 and j < columns - 1:
                        if grid[i-1][j+1] == '@':
                            rolls_adjacent += 1

                    # Check left
                    if j > 0:
                        if grid[i][j-1] == '@':
                            rolls_adjacent += 1

                    # Check right
                    if j < columns - 1:
                        if grid[i][j+1] == '@':
                            rolls_adjacent += 1

                    # Check down-left
                    if i < rows - 1 and j > 0:
                        if grid[i+1][j-1] == '@':
                            rolls_adjacent += 1

                    # Check down-mid
                    if i < rows - 1:
                        if grid[i+1][j] == '@':
                            rolls_adjacent += 1

                    # Check down-right
                    if i < rows - 1 and j < columns - 1:
                        if grid[i+1][j+1] == '@':
                            rolls_adjacent += 1

                    if rolls_adjacent < 4:
                        indexes_to_remove.append([i, j])

        if indexes_to_remove == []:
            continue_removal = False
        else:
            for r, c in indexes_to_remove:
                grid[r] = grid[r][:c] + '.' + grid[r][c+1:]   
                total += 1

    return total

def main():
    paper_grid = read_input(os.path.join(os.getcwd(), '2025\\Day4\\day4input.txt'))
    part1_ans = part1(paper_grid)
    part2_ans = part2(paper_grid)
    print(part1_ans)
    print(part2_ans)

main()