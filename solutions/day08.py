part1 = 0
part2 = 0
map_trees = []
with open('../inputs/day08.txt') as lines:
    data = lines.readlines()
    for d in data:
        map_trees.append([int(i) for i in d.rstrip()])

directions = ((-1, 0), (1, 0), (0, -1), (0, 1))  # up, down, left, right (i, j)
row_len = len(map_trees[0])
col_len = len(map_trees)
for i in range(col_len):
    for j in range(row_len):
        # if edge, continue
        if i == 0 or j == 0 or i == col_len - 1 or j == row_len - 1:
            part1 += 1
            continue
        # we look in all 4 directions from closest to farthest to the edge
        path_to_egde = [(i, 0), (col_len - i, 1), (j, 2), (row_len - j, 3)]  # left, up, down, right
        for (k, l) in sorted(path_to_egde):
            curr_x = j
            curr_y = i
            is_highest = False
            # while not at the edge
            while curr_y != 0 and curr_x != 0 and curr_x != row_len - 1 and curr_y != col_len - 1:
                curr_x += directions[l][1]
                curr_y += directions[l][0]
                # if a tree is higher, stop here and move to next direction
                if map_trees[i][j] <= map_trees[curr_y][curr_x]:
                    break
                # if we come to an edge, the tree is visible from outside
                if curr_x == 0 or curr_y == 0 or curr_x == row_len - 1 or curr_y == col_len - 1:
                    is_highest = True
            # if the tree is visible, increment part1 by one and move to next tree
            if is_highest:
                part1 += 1
                break

for i in range(col_len):
    for j in range(row_len):
        # if on the edge, continue
        if i == 0 or j == 0 or i == col_len - 1 or j == row_len - 1:
            continue
        view_dist_prod = 1
        # we look in all 4 directions from closest to farthest to the edge
        path_to_egde = [(i, 0), (col_len - i, 1), (j, 2), (row_len - j, 3)]  # left, up, down, right
        for (k, l) in sorted(path_to_egde):
            curr_x = j
            curr_y = i
            # while not at the edge
            while curr_y != 0 and curr_x != 0 and curr_x != row_len - 1 and curr_y != col_len - 1:
                curr_x += directions[l][1]
                curr_y += directions[l][0]
                # if a tree is higher, stop here and move to next direction
                if map_trees[i][j] <= map_trees[curr_y][curr_x]:
                    view_dist_prod *= (abs(curr_y - i) + abs(curr_x - j))
                    break
                # if we come to an edge, stop here and calculate view distance product
                if curr_x == 0 or curr_y == 0 or curr_x == row_len - 1 or curr_y == col_len - 1:
                    view_dist_prod *= (abs(curr_y - i) + abs(curr_x - j))
        # if this iteration is bigger than current, update current
        if view_dist_prod > part2:
            part2 = view_dist_prod

# part 1
print(part1)
# part 2
print(part2)
