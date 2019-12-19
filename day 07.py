from itertools import permutations


def get_parameter_value_with_mode(ints, ptr, param, nstring):
    mode = nstring[(-2 - param)]
    if mode == '0':  # position mode
        return ints[ints[ptr + param]]
    elif mode == '1':  # intermediate mode
        return ints[ptr + param]
    else:
        print('unknown mode ' + mode)


def intcode(phase, inputs, ints):
    # getinput = int(input("Enter initial value "))
    ptr = 0
    while ints[ptr] != 99: # loop through until we reach the end of the list, unless we find 99
        n = ints[ptr]
        nstring = str(n).zfill(4)

        if len(nstring) > 2: # checking for parameter modes
            opcode = nstring[-2:]
            if opcode == '99':
                break
            elif opcode == '01':
                x = get_parameter_value_with_mode(ints, ptr, 1, nstring)
                y = get_parameter_value_with_mode(ints, ptr, 2, nstring)
                ints[ints[ptr + 3]] = x + y
                ptr += 4

            elif opcode == '02':
                x = get_parameter_value_with_mode(ints, ptr, 1, nstring)
                y = get_parameter_value_with_mode(ints, ptr, 2, nstring)
                ints[ints[ptr + 3]] = x * y
                ptr += 4

            elif opcode == '03':
                if ptr == 0:
                    if nstring[-3] == '1':
                        ints[ptr + 1] = phase
                    else:
                        ints[ints[ptr + 1]] = phase
                    ptr += 2
                else:
                    if nstring[-3] == '1':
                        ints[ptr + 1] = inputs
                    else:
                        ints[ints[ptr + 1]] = inputs
                    ptr += 2

            elif opcode == '04':
                if nstring[-3] == '1':
                    return ints[ptr + 1]
                else:
                    return ints[ints[ptr + 1]]

            elif opcode == '05':
                value_to_check = get_parameter_value_with_mode(ints, ptr, 1, nstring)
                new_ptr = get_parameter_value_with_mode(ints, ptr, 2, nstring)
                if value_to_check != 0:  # check for nonzero
                    ptr = new_ptr
                else:
                    ptr += 3

            elif opcode == '06':
                value_to_check = get_parameter_value_with_mode(ints, ptr, 1, nstring)
                new_ptr = get_parameter_value_with_mode(ints, ptr, 2, nstring)
                if value_to_check == 0:  # check for nonzero
                    ptr = new_ptr
                else:
                    ptr += 3

            elif opcode == '07':
                #print(nstring)
                x = get_parameter_value_with_mode(ints, ptr, 1 ,nstring)
                y = get_parameter_value_with_mode(ints, ptr, 2, nstring)
                if x < y:
                    ints[ints[ptr + 3]] = 1
                else:
                    ints[ints[ptr + 3]] = 0
                ptr += 4

            elif opcode == '08':
               # print(nstring)
                x = get_parameter_value_with_mode(ints, ptr, 1, nstring)
                y = get_parameter_value_with_mode(ints, ptr, 2, nstring)
                if x == y:
                    ints[ints[ptr + 3]] = 1
                else:
                    ints[ints[ptr + 3]] = 0
                ptr += 4

            else:
                print('unknown opcode ' + opcode)
                break

# Day 7 - Part 1
perms = list(permutations([0, 1, 2, 3, 4]))  # create all permutations of phases
totals = []  # empty list to hold the totals in
for permutation in perms:
    ints = [3,8,1001,8,10,8,105,1,0,0,21,38,63,76,93,118,199,280,361,442,99999,3,9,101,3,9,9,102,3,9,9,101,4,9,9,4,9,99,3,9,1002,9,2,9,101,5,9,9,1002,9,5,9,101,5,9,9,1002,9,4,9,4,9,99,3,9,101,2,9,9,102,3,9,9,4,9,99,3,9,101,2,9,9,102,5,9,9,1001,9,5,9,4,9,99,3,9,102,4,9,9,1001,9,3,9,1002,9,5,9,101,2,9,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,99]  # sample data from website - should give 43210
    print('********* Permutation ', permutation)
    output = 0
    ans = 0
    for i in permutation:  # one loop for each phase in this permutation
        output = intcode(i, ans, ints)  # pass in current phase, running total and integers
        ans = output
    totals.append(output)

print(max(totals))

