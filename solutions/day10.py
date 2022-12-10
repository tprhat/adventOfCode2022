cnt = 1
reg = 1
part1 = 0
# matrix for part2
rows, cols = (6, 40)
matrix = [['.' for i in range(cols)] for j in range(rows)]

times = (20, 60, 100, 140, 180, 220)
times2 = (40, 80, 120, 160, 200, 240)

with open('../inputs/day10.txt') as lines:
    data = lines.readlines()
    for d in data:
        # if command is noop: move by one and sum if cnt is in times
        if d.startswith('noop'):
            cnt += 1
            if cnt in times:
                part1 += (cnt * reg)
        # if command is addx do nothing for 1 cycle and check if cnt in times (same as noop)
        # in second cycle add addx value to reg
        else:
            cnt += 1
            if cnt in times:
                part1 += (cnt * reg)
            addx = int(d.rstrip().split(' ')[1])
            reg += addx
            cnt += 1
            if cnt in times:
                part1 += (cnt * reg)
    # part 2
    curr_row, curr_col, reg_row = 0, 0, 1
    addx = 0
    reg = 1
    for d in data:

        if d.startswith('noop'):
            # update matix if curr_row in (reg_row +- 1)
            if curr_row in (reg_row - 1, reg_row, reg_row + 1):
                matrix[curr_col][curr_row] = '#'
            # move row by one
            curr_row += 1
            # check if at row end
            if curr_row == 40:
                curr_row = 0
                curr_col += 1
        # addx command
        else:
            # first cycle
            # update matix if curr_row in (reg_row +- 1)
            if curr_row in (reg_row - 1, reg_row, reg_row + 1):
                matrix[curr_col][curr_row] = '#'
            curr_row += 1
            if curr_row == 40:
                curr_row = 0
                curr_col += 1
            # second cycle
            if curr_row in (reg_row - 1, reg_row, reg_row + 1):
                matrix[curr_col][curr_row] = '#'
            addx = int(d.rstrip().split(' ')[1])
            # move reg by addx
            reg += addx
            # check if over the end
            reg_row = reg % 40

            curr_row += 1
            # update if curr_row at the end
            if curr_row == 40:
                curr_row = 0
                curr_col += 1
print(part1)
for row in matrix:
    print()
    for v in row:
        print(v, end='')
part2 = 'EHBZLRJK'
print(f'\n{part2}')
