sum1 = 0
sum2 = 0
with open('../inputs/day03.txt') as lines:
    group = []
    for line in lines:
        # part 1
        n = len(line)
        a, b = line[:n // 2], line[n // 2:]
        l1, l2 = '', ''
        for i in a:
            if i in b:
                l1 = i
                break
        if l1.isupper():
            sum1 += ord(l1) - ord('A') + 27
        else:
            sum1 += ord(l1) - ord('a') + 1
        # part 2
        group.append(line)
        if len(group) == 3:
            for i in group[0]:
                if i in group[1] and i in group[2]:
                    l2 = i
                    break
            if l2.isupper():
                sum2 += ord(l2) - ord('A') + 27
            else:
                sum2 += ord(l2) - ord('a') + 1
            group.clear()

# part 1
print(sum1)

# part 2
print(sum2)
