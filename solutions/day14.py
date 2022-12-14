from itertools import count, product


# return all sand positions possible
def draw(x1, y1, x2, y2):
    if x1 > x2:
        return draw(x2, y1, x1, y2)
    if y1 > y2:
        return draw(x1, y2, x2, y1)
    return product(range(x1, x2 + 1), range(y1, y2 + 1))


# ways in which sand can move
def adj(x, y):
    return (x, y + 1), (x - 1, y + 1), (x + 1, y + 1)


def part1(f):
    rocks = set()
    for line in f:
        pts = line.split(' -> ')
        # zip pts[0], pts[1]; pts[1], pts[2]...
        for a, b in zip(pts, pts[1:]):
            # *eval(a) unpacks values from eval since eval returns (498,4), *eval returns 498,4
            rocks.update(draw(*eval(a), *eval(b)))

    max_y = max(y for _, y in rocks)
    # start = 500, 0
    for i in count():
        curr = 500, 0
        # depth curr is smaller than max_y
        while curr[1] < max_y:
            try:
                # get next from iterator
                # try moving sand down, down-left, down-right if not in rocks
                curr = next(x for x in adj(*curr) if x not in rocks)
            # StopIteration waits for Signal the end from iterator.__next__().
            except StopIteration:
                break
        # if except does not break the loop, and it ends 'naturally', return count of sand
        else:
            return i
        # add current sand particle to rocks set
        rocks.add(curr)


def part2(f):
    rocks = set()
    for line in f:
        pts = line.split(' -> ')
        # zip pts[0], pts[1]; pts[1], pts[2]...
        for a, b in zip(pts, pts[1:]):
            # *eval(a) unpacks values from eval since eval returns (498,4), *eval returns 498,4
            rocks.update(draw(*eval(a), *eval(b)))

    max_y = max(y for _, y in rocks)
    start = 500, 0
    for i in count():
        curr = start

        while True:
            try:
                # get next from iterator
                # try moving sand down, down-left, down-right if not in rocks
                # and depth of sand is smaller than max_y + 2
                curr = next(x for x in adj(*curr) if x not in rocks and x[1] < max_y + 2)
            except StopIteration:
                break
        # if while True does not update curr, it means we reached the top
        # return i + 1
        if curr == start:
            return i + 1
        # add current sand particle to rocks set
        rocks.add(curr)


file = open('../inputs/day14.txt').read().split('\n')
part1 = part1(file)
part2 = part2(file)
print(part1)
print(part2)
