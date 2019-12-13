from math import atan2

with open('C:/Users/ar206747/OneDrive - Falmouth University/Programming/AoC 2019/10.in.txt') as f:
    space = [line.strip() for line in f]
angles = {}
asteroids = []
for y, line in enumerate(space):
    for x, char in enumerate(line):
        if char == '#':
            asteroids.append((x, y))


for (ax, ay) in asteroids:
    # print(ax, ay)
    for (ox, oy) in asteroids:
        if (ax, ay) == (ox, oy):
            continue
        angle = atan2((ay - oy), (ax - ox))
        if (ax, ay) not in angles:
            angles[(ax, ay)] = [angle]
        else:
            angles[(ax, ay)].append(angle)

m = 0
chosenasteroid = ()
for asteroid in angles:
    total = len(set(angles[asteroid]))
    if total > m:
        m = total
        chosenasteroid = asteroid

# best location for the base is (31, 20)

# part 2

print(angles[(31, 20)])