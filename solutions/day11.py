from math import floor

from math import prod


# Monkey class
class Monkey:
    def __init__(self, x):
        x = x.split('\n')
        self.items = [*map(int, x[1][18:].split(','))]
        self.op = eval(f'lambda old: {x[2][19:]}') # old = old +* int
        self.div = int(x[3][20:])
        self.true = int(x[4][28:])
        self.false = int(x[5][29:])
        self.act = 0


# unpack map function mappings to list
ms1 = [*map(Monkey, open("../inputs/day11.txt").read().split('\n\n'))]
ms2 = [*map(Monkey, open("../inputs/day11.txt").read().split('\n\n'))]

# least common multiple
# if we first do MOD p and then MOD self.dive we speed up the execution
p = prod(m.div for m in ms2)

for _ in range(20):
    for m in ms1:
        for worry in m.items:
            worry = floor(m.op(worry) / 3)
            dest = m.false if worry % m.div else m.true
            ms1[dest].items += [worry]
            m.act += 1
        m.items = []

for _ in range(10_000):
    for m in ms2:
        for worry in m.items:
            worry = m.op(worry) % p
            dest = m.false if worry % m.div else m.true
            ms2[dest].items += [worry]
            m.act += 1
        m.items = []

# part 1
print(prod(sorted(m.act for m in ms1)[-2:]))

# part 2
print(prod(sorted(m.act for m in ms2)[-2:]))
