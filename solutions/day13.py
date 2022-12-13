import json


# compare function 
def compare(p1, p2):
    for i in range(min(len(p1), len(p2))):
        # if both int, compare as ints
        if isinstance(p1[i], int) and isinstance(p2[i], int):
            if p1[i] == p2[i]:
                continue
            return p1[i] < p2[i]
        # if one is list, compare as lists
        elif isinstance(p1[i], int) or isinstance(p2[i], int):
            if isinstance(p1[i], int):
                res = compare([p1[i]], p2[i])
            else:
                res = compare(p1[i], [p2[i]])
            if not res:
                continue
            return res
        else:  # both list
            res = compare(p1[i], p2[i])
            if not res:
                continue
            return res

    if len(p1) != len(p2):
        return len(p1) < len(p2)


def part1():
    pairs = open("../inputs/day13.txt").read().split('\n\n')
    total = 0
    i = 1
    for pair in pairs:
        p = pair.split('\n')
        # json.loads - loads string data into a python object
        if compare(json.loads(p[0]), json.loads(p[1])):
            total += i
        i += 1

    print(total)


def part2():
    input_list = list(map(json.loads, open("../inputs/day13.txt").read().replace('\n\n', '\n').split('\n')))
    # create dividers
    divider1 = json.loads('[[2]]')
    divider2 = json.loads('[[6]]')
    # cnt of how many nums come before every divider
    divider1_pos = 1  # 1-indexed
    divider2_pos = 1  # 1-indexed
    # append dividers
    input_list.append(divider1)
    input_list.append(divider2)
    # compare each and
    for p in input_list:
        if compare(p, divider1):
            divider1_pos += 1
        if compare(p, divider2):
            divider2_pos += 1
    # result
    print(divider1_pos * divider2_pos)


part1()
part2()
