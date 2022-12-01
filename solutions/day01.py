list_sums = []
with open('inputs/day01.txt') as lines:
    sum_lines = 0
    for line in lines:
        if line == '\n':
            list_sums.append(sum_lines)
            sum_lines = 0
        else:
            sum_lines += int(line)
# part 1
print(max(list_sums))

# part 2
print(sum(sorted(list_sums, reverse=True)[0:3]))
