
from collections import deque

planets = {}
for line in open('6.in').readlines():
    a, b = line.strip().split(')')
    if a not in planets:
        planets[a] = []
    if b not in planets:
        planets[b] = []
    planets[a].append(b)
    planets[b].append(a)

D = {}
Q = deque()
Q.append(('YOU', 0))
while Q:
    x, d = Q.popleft()
    if x in D:
        continue
    D[x] = d
    for y in planets[x]:
        Q.append((y, d + 1))
print(D['SAN'])


def countchildren(planet):
    ans = 0
    for child in planets.get(planet, []):
        ans += countchildren(child)
        ans += 1
    return ans

#ans = 0
#for planet in planets:
#    ans += countchildren(planet)

#print(ans)


