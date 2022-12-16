import math
import re
from collections import defaultdict
from functools import cache

# regex to find needed values
REGEX = r"^Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? ([\w ,]+)$"


def parse_input(f):
    valves = {}
    # dict inside a dict with default value of +inf
    # it contains all the distances from one valve to other valves
    dist = defaultdict(lambda: defaultdict(lambda: math.inf))
    for i, flow_rate, tunnels in re.findall(REGEX, f.read(), re.MULTILINE):
        valves[i] = int(flow_rate)
        dist[i][i] = 0
        for j in tunnels.split(', '):
            dist[i][j] = 1

    # find the shortest path from each valve to other valves
    for k in valves:
        for i in valves:
            for j in valves:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return valves, dist


def part1(valves, dist):
    @cache
    def dp(starting_valve, time, remaining):
        ans = 0
        # remaining has all the unopenend valves
        for j in remaining:
            # if current time - time to reach a valve - 1 >= 0
            if (next_time := time - dist[starting_valve][j] - 1) >= 0:
                # sum the flow rate of a valve we opened over time
                # + dp(current_valve, time left, remaining unopened valves)
                ans = max(ans, valves[j] * next_time + dp(j, next_time, remaining - {j}))
        return ans

    # start at 'AA', 30 minutes, all valves with flow rate > 0
    return dp('AA', 30, frozenset(x for x in valves if valves[x] > 0))


def part2(valves, dist):
    @cache
    def dp(starting_valve, time, remaining, elephant):
        # if we have an elephant time is reduced to 26
        ans = dp('AA', 26, remaining, False) if elephant else 0
        for j in remaining:
            # if current time - time to reach a valve - 1 >= 0
            # sum the flow rate of a valve we opened over time
            # + dp(current_valve, time left, remaining unopened valves)
            if (next_time := time - dist[starting_valve][j] - 1) >= 0:
                # sum the flow rate of a valve we opened over time
                # + dp(current_valve, time left, remaining unopened valves)
                ans = max(ans, valves[j] * next_time + dp(j, next_time, remaining - {j}, elephant))
        return ans

    # start at 'AA', 30 minutes, all valves with flow rate > 0, elephant=True
    return dp('AA', 26, frozenset(x for x in valves if valves[x] > 0), True)


valves, dist = parse_input(open('../inputs/day16.txt'))
part1 = part1(valves, dist)
print(part1)

part2 = part2(valves, dist)
print(part2)
