from sys import stdin
from collections import defaultdict

n = int(stdin.readline())  # number of nodes
parents = list(map(int, stdin.readline().split()))  # parents of each nodes

# make dict for children nodes
children = defaultdict(list)
for i, parent in enumerate(parents):
    children[parent].append(i)

target = int(stdin.readline())  # node to be removed
# stack for nodes to be removed
targets = [target]
# remove first target node in children list of parent dict
if target in children.keys():
    children[parents[target]].remove(target)

removed = []  # removed nodes
# remove nodes in dict
while targets:
    cur = targets.pop()
    if cur in children.keys():
        targets += children[cur]
        children.pop(cur)
    removed.append(cur)

# count leaf nodes
result = 0
for i in range(n):
    if i not in removed and (i not in children.keys() or not children[i]):
        result += 1

print(result)

"""
틀림
"""