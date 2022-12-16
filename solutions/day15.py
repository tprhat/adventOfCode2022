import z3


def parse_input(f):
    sensors = []
    for line in f.read().strip().splitlines():
        left, right = line.split(': ')
        sensor_x = int(left.split(', ')[0].split('=')[1])
        sensor_y = int(left.split(', ')[1].split('=')[1])
        beacon_x = int(right.split(', ')[0].split('=')[1])
        beacon_y = int(right.split(', ')[1].split('=')[1])

        sensors.append((sensor_x, sensor_y, beacon_x, beacon_y))
    # set of all beacons
    beacons = set()
    m = {}
    # m is a dict with keys being sensor x and y, and values are distances to the closest beacon
    for sx, sy, bx, by in sensors:
        d = abs(sx - bx) + abs(sy - by)
        m[(sx, sy)] = d
        beacons.add((bx, by))

    return sensors, beacons, m


def part1(sensors, beacons, m, y_target):
    res = 0
    # find number or position in which the beacon cannot be
    # with x being anything in range -5e6 and 5e6, and y = y_target
    for x in range(int(-5e6), int(5e6)):
        good = True
        for sx, sy, _, _ in sensors:
            dist = abs(x - sx) + abs(sy - y_target)
            # if dist is less or equal to min dist from sensor break the loop
            if dist <= m[(sx, sy)]:
                good = False
                break
        if not good:
            # if there is not already a beacon at those coordinates, res += 1
            if (x, y_target) not in beacons:
                res += 1
    return res


def part2(sensors, m, bound):
    # find beacon's coordinates gives the constraints
    # mathematical solver for SAT problem
    s = z3.Solver()
    # define what type of variables are x and y
    x, y = z3.Int('x'), z3.Int('y')
    # add basic constaints
    s.add(x >= 0)
    s.add(x <= bound)
    s.add(y >= 0)
    s.add(y <= bound)
    # add constaints based on distance
    for sx, sy, bx, by in sensors:
        my_dist = z3.Abs(sx - x) + z3.Abs(sy - y)
        # dist must be grater than min distance for each sensor
        s.add(my_dist > m[(sx, sy)])
        # and x and y are not already a beacon
        s.add(z3.And(x != bx, y != by))
    # check if the problem is satisfied
    assert s.check() == z3.sat
    # create a model
    m = s.model()
    # return x and y
    return m[x].as_long(), m[y].as_long()


file = open('../inputs/day15.txt')
sensors, beacons, dist = parse_input(file)

part1 = part1(sensors, beacons, dist, 2000000)
print(part1)
p2_x, p2_y = part2(sensors, dist, 4000000)
print(p2_x * 4000000 + p2_y)
