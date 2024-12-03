def read_input(file):
    report_list = []
    with open(file) as f: 
        lines = f.readlines()
        for line in lines:
            report_list.append(list(map(int, line.split()))) # Turns each report into a list of integers and adds to a list containing all reports
    return report_list

def part1(reports):
    total_safe = 0
    for report in reports:
        report_safe = all(i < j for i, j in zip(report, report[1:])) or all(i > j for i, j in zip(report, report[1:])) # Checks if list is strictly increasing or decreasing
        if report_safe:
            for i, j in zip(report, report[1:]):
                if not (1 <= abs(i - j) <= 3): # Checks if report meets >0 <=3 constraint 
                    report_safe = False
                    break
        if report_safe:
            total_safe += 1
    return total_safe

def part2(reports):
    total_safe = 0
    for report in reports:
        report_safe = [False for i in range(len(reports))]
        for k in range(len(report)):
            damp_report = report[:k] + report[k+1:] # Makes a 'damp report' removing one level from the report and then checks the same way as part1
            report_safe[k] = all(i < j for i, j in zip(damp_report, damp_report[1:])) or all(i > j for i, j in zip(damp_report, damp_report[1:])) # Checks if list is strictly increasing or decreasing
            if report_safe[k]:
                for i, j in zip(damp_report, damp_report[1:]):
                    if not (1 <= abs(i - j) <= 3): # Checks if report meets >0 <=3 constraint 
                        report_safe[k] = False
                        break
        if any(report_safe):
            total_safe += 1
    return total_safe

def main():
    report_list = read_input('day2input.txt')
    part1_ans = part1(report_list)
    print(part1_ans)
    part2_ans = part2(report_list)
    print(part2_ans)

main()