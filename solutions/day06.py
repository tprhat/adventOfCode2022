p1, p2 = 0, 0
seq1, seq2 = [], []
with open('../inputs/day06.txt') as lines:
    data = lines.readline()
    for char in data:
        if len(seq1) != 4:
            seq1.append(char)
            p1 += 1

        elif len(set(seq1)) == 4:
            break
        else:
            seq1.pop(0)
            seq1.append(char)
            p1 += 1

    # part 2
    for char in data:
        if len(seq2) != 14:
            seq2.append(char)
            p2 += 1

        elif len(set(seq2)) == 14:
            break
        else:
            seq2.pop(0)
            seq2.append(char)
            p2 += 1

# part 1
print(p1)
# part 2
print(p2)
