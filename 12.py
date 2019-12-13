moons = []
velocities = []
for line in open('12.in').readlines():
    line = line.strip()
    line = line[1:-1]
    words = line.split()
    moon = {}
    for w in words:
        k, v = w.split('=')
        if v.endswith(','):
            v = v[:-1]
        moon[k] = int(v)
    moons.append(moon)
    velocities.append({'x': 0, 'y': 0, 'z': 0})
moons2 = moons[:]
velocities2 = velocities[:]
for t in range(1000):
    for moon in range(len(moons)):  # loop through moons
        for other in range(len(moons)):  # loop through other moons to compare
            for val in moons[moon]:  # for each coordinate
                if moons[moon][val] < moons[other][val]:
                    velocities[moon][val] += 1
                if moons[moon][val] > moons[other][val]:
                    velocities[moon][val] -= 1
    for i in range(len(moons)):
        for val in moons[i]:
            moons[i][val] += velocities[i][val]

# part 1 answer
totalenergy = 0
for i in range(len(moons)):
    penergy = 0
    kenergy = 0
    for val in moons[i]:
        penergy += abs(moons[i][val])
        kenergy += abs(velocities[i][val])
    totalenergy += kenergy * penergy
print(totalenergy)

# part 2

t = 0
z = 0
moonval = ''
matches = {}
matchcounter = {}
found = False
while True:
    while z < 3:
        if z == 0:
            xyz = 'x'
        elif z == 1:
            xyz = 'y'
        elif z == 2:
            xyz = 'z'
        moons = moons2[:]
        velocities = velocities2[:]  # take fresh copies of original positions
        while True:
            if z not in matches:
                matches[z] = []

            for moon in range(len(moons)):  # loop through moons
                for other in range(len(moons)):  # loop through other moons to compare
                    for val in moons[moon]:  # for each coordinate
                        if moons[moon][val] < moons[other][val]:
                            velocities[moon][val] += 1
                        if moons[moon][val] > moons[other][val]:
                            velocities[moon][val] -= 1
            for i in range(len(moons)):
                for val in moons[i]:
                    moons[i][val] += velocities[i][val]
            moonval = ''

            for l in range(len(moons)):
                print(moons)
                moonval += str(moons[l][xyz])
            if moonval not in matches[z]:
                matches[z].append(moonval)
            else:
                matchcounter[z] = t
                z += 1
            t += 1  #may need to move this to the top of the loop
    break

print(matchcounter)