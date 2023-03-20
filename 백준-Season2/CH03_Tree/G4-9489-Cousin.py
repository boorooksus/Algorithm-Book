from sys import stdin
from collections import defaultdict, deque
input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    while True:
        n, K = map(int, input().split())
        if n == 0 and K == 0:
            break
        seq = list(map(int, input().split()))

        children = defaultdict(list)
        parents = defaultdict(int)
        parents[seq[0]] = -1
        dq = deque([seq[0]])
        i = 1
        while i < len(seq):
            parent = dq.popleft()
            j = i + 1
            while j < len(seq) and seq[j - 1] + 1 == seq[j]:
                j += 1
            for k in range(i, j):
                children[parent].append(seq[k])
                parents[seq[k]] = parent
                dq.append(seq[k])
            i = j

        ans = 0
        parent = parents[K]
        for prev in children[parents[parent]]:
            if prev != parent:
                ans += len(children[prev])

        print(ans)

"""
        0
     1                   2
  3  4  5               6
 7 8 / 9 10 / 11 


"""