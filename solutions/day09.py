visited1 = set()
s, T, H = (0, 0), (0, 0), (0, 0)
T2 = [(0, 0) for i in range(9)]
visited1.add(s)
visited2 = visited1.copy()
directions = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (1, 0),
    'D': (-1, 0)
}
with open('../inputs/day09.txt') as lines:
    data = lines.readlines()
    for d in data:
        direction, cnt = d.rstrip().split()[0], int(d.rstrip().split()[1])

        for _ in range(cnt):
            # Move H in the desired direction
            x = H[0] + directions[direction][0]
            y = H[1] + directions[direction][1]
            H = (x, y)
            # if T is 2 position vertically or horizontally move T accordingly
            if abs(T[0] - H[0]) >= 2 or abs(T[1] - H[1]) >= 2:
                t1 = 0
                t2 = 0
                if H[0] - T[0] >= 2:
                    t1 = 1
                elif H[0] - T[0] <= -2:
                    t1 = -1
                if H[1] - T[1] >= 2:
                    t2 = 1
                elif H[1] - T[1] <= -2:
                    t2 = -1
                T = (T[0] + (H[0] - T[0] - t1), T[1] + (H[1] - T[1] - t2))
            # add T to visited
            visited1.add(T)
    # reset H to start for part 2
    H = (0, 0)
    for d in data:
        direction, cnt = d.rstrip().split()[0], int(d.rstrip().split()[1])

        for _ in range(cnt):
            # Move H in the desired direction
            x = H[0] + directions[direction][0]
            y = H[1] + directions[direction][1]
            H = (x, y)
            # Move other 9 tails if necessary
            for i in range(9):
                # if i == 0 -> first tail, compare it to H
                if i == 0:
                    if abs(T2[0][0] - H[0]) >= 2 or abs(T2[0][1] - H[1]) >= 2:
                        t1 = 0
                        t2 = 0
                        if H[0] - T2[0][0] >= 2:
                            t1 = 1
                        elif H[0] - T2[0][0] <= -2:
                            t1 = -1
                        if H[1] - T2[0][1] >= 2:
                            t2 = 1
                        elif H[1] - T2[0][1] <= -2:
                            t2 = -1
                        T2[0] = (T2[0][0] + (H[0] - T2[0][0] - t1), T2[0][1] + (H[1] - T2[0][1] - t2))
                # else compare i tail to i - 1 tail
                else:
                    if abs(T2[i][0] - T2[i - 1][0]) >= 2 or abs(T2[i][1] - T2[i - 1][1]) >= 2:
                        t1 = 0
                        t2 = 0
                        if T2[i - 1][0] - T2[i][0] >= 2:
                            t1 = 1
                        elif T2[i - 1][0] - T2[i][0] <= -2:
                            t1 = -1
                        if T2[i - 1][1] - T2[i][1] >= 2:
                            t2 = 1
                        elif T2[i - 1][1] - T2[i][1] <= -2:
                            t2 = -1
                        T2[i] = (T2[i][0] + (T2[i - 1][0] - T2[i][0] - t1), T2[i][1] + (T2[i - 1][1] - T2[i][1] - t2))
                # add last tail to visited
                if i == 8:
                    visited2.add(T2[8])

part1 = len(visited1)
part2 = len(visited2)
# part 1
print(part1)
# part 2
print(part2)
