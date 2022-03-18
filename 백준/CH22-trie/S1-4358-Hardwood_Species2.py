from collections import defaultdict
import sys

cnts = defaultdict(int)
total = 0
lines = sys.stdin.readlines()
for line in lines:
    cnts[line.strip()] += 1
    total += 1

for specy in sorted(cnts.keys()):
    print("%s %.4f" % (specy, cnts[specy] / total * 100))