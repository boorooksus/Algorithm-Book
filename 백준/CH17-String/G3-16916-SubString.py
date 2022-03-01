from sys import stdin


# s = stdin.readline().rstrip()
# p = stdin.readline().rstrip()
# print([0, 1][s.__contains__(p)])

sp = [stdin.readline().rstrip() for _ in range(2)]
print([0, 1][sp[1] in sp[0]])
