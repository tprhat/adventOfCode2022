points_by_play = {
    'X': [4, 1, 7],  # rock
    'Y': [8, 5, 2],  # paper
    'Z': [3, 9, 6]   # scissors
}
opponent = {
    'A': 0,  # rock
    'B': 1,  # paper
    'C': 2   # scissors
}

points_by_play2 = {
    'A': [3, 4, 8],  # rock
    'B': [1, 5, 9],  # paper
    'C': [2, 6, 7]   # scissors
}
opponent2 = {
    'X': 0,  # lose
    'Y': 1,  # draw
    'Z': 2   # win
}

sum_strategy = 0
sum_strategy2 = 0
with open('../inputs/day02.txt') as lines:
    for line in lines:
        p1, p2 = line.split()
        sum_strategy += points_by_play[p2][opponent[p1]]
        sum_strategy2 += points_by_play2[p1][opponent2[p2]]
# part1
print(sum_strategy)

# part2
print(sum_strategy2)
