import copy

with open('../inputs/day05.txt') as lines:
    data = lines.readlines()
    init_phase = True
    stack1 = [[] for _ in range(9)]
    stack2 = [[] for _ in range(9)]
    for line in data:
        if line == '\n':
            continue
        if line.startswith(' 1'):
            init_phase = False
            stack2 = copy.deepcopy(stack1)
            continue
        # initialize stack1
        if init_phase:
            i = 0
            j = 0
            while i < len(line):
                if line[i] == '[':
                    stack1[j].append(line[i + 1])
                j += 1
                i += 4

        if not init_phase:
            action = line.split(' ')
            cnt, start, dest = int(action[1]), int(action[3]), int(action[5])
            helper = []
            for _ in range(cnt):
                # 0 - indexed
                stack1[dest - 1].insert(0, stack1[start - 1].pop(0))
                helper.append(stack2[start - 1].pop(0))
            # insert in reverse order to stack2
            for _ in reversed(helper):
                stack2[dest - 1].insert(0, _)

    part1 = ''
    part2 = ''
    for i in range(len(stack1)):
        if stack1[i]:
            part1 += stack1[i][0]
        if stack2[i]:
            part2 += stack2[i][0]

# part 1
print(part1)

# part 2
print(part2)