from sys import stdin


wheels = ['']
for i in range(4):
    wheels.append(stdin.readline())
n = int(stdin.readline())
rotations = []
for i in range(n):
    rotations.append(tuple(map(int, stdin.readline().split())))

tops = [0 for _ in range(5)]

for wheel, drc in rotations:
    prev_pole = wheels[wheel][(tops[wheel] + 2) % 8]
    prev_dir = drc
    i = wheel + 1
    while i < len(wheels):
        cur_pole = wheels[i][(tops[i] + 6) % 8]

        if prev_pole == cur_pole:
            break

        prev_pole = wheels[i][(tops[i] + 2) % 8]
        prev_dir *= -1
        tops[i] = (tops[i] - prev_dir) % 8
        i += 1

    prev_pole = wheels[wheel][(tops[wheel] + 6) % 8]
    prev_dir = drc
    i = wheel - 1
    while i > 0:
        cur_pole = wheels[i][(tops[i] + 2) % 8]

        if prev_pole == cur_pole:
            break

        prev_pole = wheels[i][(tops[i] + 6) % 8]
        prev_dir *= -1
        tops[i] = (tops[i] - prev_dir) % 8
        i -= 1
    tops[wheel] = (tops[wheel] - drc) % 8


print(sum([2 ** (i - 1) * int(wheels[i][tops[i]]) for i in range(1, 5)]))
