from sys import stdin
from itertools import combinations


def main():
    x = list(stdin.readline().rstrip())
    stack, brackets = [], []

    for i, char in enumerate(x):
        if char == '(':
            stack.append(i)
        elif char == ')':
            brackets.append([stack.pop(), i])

    res = set()
    for i in range(1, len(brackets) + 1):
        for comb in combinations(brackets, i):
            new = x[:]
            for o, c in comb:
                new[o], new[c] = '', ''
            res.add(''.join(new))

    print(*sorted(list(res)), sep='\n')


if __name__ == "__main__":
    main()
