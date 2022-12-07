from collections import defaultdict

dir_hierarchy = defaultdict(list)
dir_size = defaultdict(int)
with open('../inputs/day07.txt') as lines:
    data = lines.readlines()
    cwd = ''
    i = 1
    while i < len(data):
        if data[i].startswith('$'):  # command
            command = data[i].split()[1:]
            if command[0] == 'cd':
                if command[1] == '..':
                    cwd = '/'.join(cwd.split('/')[:-1])
                else:
                    if cwd == '':
                        dir_hierarchy['/'].append('/' + command[1])
                    else:
                        dir_hierarchy[cwd].append(cwd + '/' + command[1])
                    cwd += f'/{command[1]}'
                i += 1
            elif command[0] == 'ls':
                j = i + 1
                while j < len(data) and not data[j].startswith('$'):
                    if data[j][0].isdigit():
                        if cwd == '':
                            cwd_where = '/'
                        else:
                            cwd_where = cwd
                        dir_size[cwd_where] += int(data[j].split()[0])
                    j += 1
                i = j
for keys, values in reversed(dir_hierarchy.items()):
    for curr_dir in values:
        dir_size[keys] += dir_size[curr_dir]  # add curr_dir size to its parent's size
part1 = sum(i for i in dir_size.values() if i < 100000)
part2 = min(list(i for i in dir_size.values() if dir_size['/'] - i <= 40000000))

# part 1
print(part1)
# part 2
print(part2)
