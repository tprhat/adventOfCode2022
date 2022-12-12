def bfs(start):
    queue, visited = [[start]], {start}
    # while there are still paths in queue
    while queue:
        path = queue.pop(0)
        i, j = path[-1]
        # if we found the top return path
        if matrix[i][j] == "E":
            return path
        # for all directions
        for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            # if not outside of board and height diff at most +1 and not yet visited
            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and f(matrix[x][y]) - f(matrix[i][j]) < 2 and (
                    x, y) not in visited:
                # add new path to queue
                queue.append(path + [(x, y)])
                # add x, y to visited
                visited.add((x, y))


def f(x):
    if x not in 'SE':
        return ord(x)
    elif x == 'S':
        return ord('a')
    else:
        return ord('z')


matrix = [list(x.strip()) for x in open('../inputs/day12.txt').readlines()]
for part in ['S', 'aS']:
    # find starting positions for the first part: 'S', and for the second part: any 'a' or 'S'
    starts = [(i, j) for j in range(len(matrix[0])) for i in range(len(matrix)) if matrix[i][j] in part]
    # find min path for both parts and prints lengths
    print(min(len(path) - 1 for s in starts if (path := bfs(s)) is not None))
