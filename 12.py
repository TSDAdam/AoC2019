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


totalenergy = 0
for i in range(len(moons)):
    penergy = 0
    kenergy = 0
    for val in moons[i]:
        penergy += abs(moons[i][val])
        kenergy += abs(velocities[i][val])
    totalenergy += kenergy * penergy
print(totalenergy)
