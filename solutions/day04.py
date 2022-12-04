cnt1 = 0
cnt2 = 0
with open('../inputs/day04.txt') as lines:
    for line in lines:
        w1, w2 = line.split(',')
        w1_start, w1_stop = w1.split('-')
        w2_start, w2_stop = w2.split('-')
        w1_start, w1_stop, w2_start, w2_stop = int(w1_start), int(w1_stop), int(w2_start), int(w2_stop)
        # part 1
        if (w1_start <= w2_start and w1_stop >= w2_stop) or (w1_start >= w2_start and w1_stop <= w2_stop):
            cnt1 += 1
        # part 2
        if w2_start <= w1_start <= w2_stop or w2_start <= w1_stop <= w2_stop \
                or w1_start <= w2_start <= w1_stop or w1_start <= w2_stop <= w1_stop:
            cnt2 += 1

# part 1
print(cnt1)

# part 2
print(cnt2)
