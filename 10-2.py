from math import atan2, sqrt

with open('C:/Users/ar206747/OneDrive - Falmouth University/Programming/AoC 2019/10.in.txt') as f:
    space = [line.strip() for line in f]
angles = {}
asteroids = []
for y, line in enumerate(space):
    for x, char in enumerate(line):
        if char == '#':
            asteroids.append((x, y))

# create all asteroid angles for part 1
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

# part 2
inLOS = {}
sortedlist = []
x, y = 31, 20
for (ax, ay) in asteroids:
    if (x, y) == (ax, ay):
        continue
    angle = atan2((x - ax), (y - ay)) # arguments reversed for CCW rotation
    distance = sqrt(((ax - x) ** 2) + ((ay - y) ** 2))  # calculate distance to asteroid
    if angle not in inLOS:  # only add if angle hasn't been used before i.e. is the first in line of sight 
        inLOS[angle] = (ax, ay, distance)
    elif angle in inLOS:
        if distance < inLOS[angle][2]:  # if the distance to this is less than the recorded distance for this angle
            print('deleting ', angle, inLOS[angle][2])
            del inLOS[angle]
            print('adding', ax, ay, distance)
            inLOS[angle] = (ax, ay, distance)


for key in sorted(inLOS, reverse=True):  # should order them highest to lowest 
    sortedlist.append((key, inLOS[key]))

for i, n in enumerate(sortedlist):
    print(i, n)

# part 1
m = 0
chosenasteroid = ()
for asteroid in angles:
    total = len(set(angles[asteroid]))
    if total > m:
        m = total
        chosenasteroid = asteroid
# best location for the base is (31, 20)

