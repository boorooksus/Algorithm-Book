from sys import stdin


print(bin(int(stdin.readline()) + 1)[3:].replace('0', '4').replace('1', '7'))
