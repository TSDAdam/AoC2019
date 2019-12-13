def intcode(ints):
    intpos1, intpos2, intpos3 = 0, 0, 0
    i = 0
    for n in ints[::4]: # step through in 4s
        intpos1 = ints[i + 1] # grab the indices for the next group of 4
        intpos2 = ints[i + 2] #
        intpos3 = ints[i + 3] #
        if n == 99:
            break
        elif n == 1:
            ints[intpos3] = ints[intpos1] + ints[intpos2]
        elif n == 2:
            ints[intpos3] = ints[intpos1] * ints[intpos2]
        i += 4
    return ints[0]

def findvalues():
    de = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,19,5,23,1,23,6,27,2,9,27,31,1,5,31,35,1,35,10,39,1,39,10,43,2,43,9,47,1,6,47,51,2,51,6,55,1,5,55,59,2,59,10,63,1,9,63,67,1,9,67,71,2,71,6,75,1,5,75,79,1,5,79,83,1,9,83,87,2,87,10,91,2,10,91,95,1,95,9,99,2,99,9,103,2,10,103,107,2,9,107,111,1,111,5,115,1,115,2,119,1,119,6,0,99,2,0,14,0]
    for i in range(0, 100):    
        for v in range(0, 100):
            p = de[:]
            p[1] = i
            p[2] = v
            #print(p, de)
            #print(intcode(p))
            if intcode(p) == 19690720:
              print(i * 100 + v)


findvalues()