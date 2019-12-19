def get_parameter_value_with_mode(ints, ptr, param, nstring):
    mode = nstring[(-2 - param)]
    if mode == '0':  # position mode
        return ints[ints[ptr + param]]
    elif mode == '1':  # intermediate mode
        return ints[ptr + param]
    else:
        print('unknown mode ' + mode)

def intcode(ints):
    getinput = int(input("Enter initial value "))
    ptr = 0
    while ints[ptr] != 99: # loop through until we reach the end of the list, unless we find 99
        n = ints[ptr]
        nstring = str(n).zfill(4)

        if len(nstring) > 2: # checking for parameter modes
            print('n = ' + nstring)
            opcode = nstring[-2:]
            print('opcode = ' + opcode)
            if opcode == '99':
                break
            elif opcode == '01':
                print(nstring)
                if nstring[-3] == '1' and nstring[-4] == '1': # are both immediate?
                    ints[ints[ptr + 3]] = ints[ptr + 1] + ints[ptr + 2] 
                elif nstring[-3] == '1': # ..or just the first
                    ints[ints[ptr + 3]] = ints[ptr + 1] + ints[ints[ptr + 2]]
                elif nstring[-4] == '1': # or just the second
                    ints[ints[ptr + 3]] = ints[ints[ptr + 1]] + ints[ptr + 2]
                else: # or none
                    ints[ints[ptr + 3]] = ints[ints[ptr + 1]] + ints[ints[ptr + 2]]
                ptr += 4

            elif opcode == '02':
                if nstring[-3] == '1' and nstring[-4] == '1':
                    ints[ints[ptr + 3]] = ints[ptr + 1] * ints[ptr + 2]
                elif nstring[-3] == '1':
                    ints[ints[ptr + 3]] = ints[ptr + 1] * ints[ints[ptr + 2]]
                elif nstring[-4] == '1':
                    ints[ints[ptr + 3]] = ints[ints[ptr + 1]] * ints[ptr + 2]
                else:
                    ints[ints[ptr + 3]] = ints[ints[ptr + 1]] * ints[ints[ptr + 2]]
                ptr += 4

            elif opcode == '03':
                if nstring[-3] == '1':
                    ints[ptr + 1] = getinput
                else:
                    ints[ints[ptr + 1]] = getinput
                ptr += 2

            elif opcode == '04':
                if nstring[-3] == '1':
                    print(ints[ptr + 1])
                else:
                    print(ints[ints[ptr + 1]])
                ptr += 2

            elif opcode == '05':
                print(nstring)
                value_to_check = get_parameter_value_with_mode(ints, ptr, 1, nstring)
                new_ptr = get_parameter_value_with_mode(ints, ptr, 2, nstring)
                if value_to_check != 0:  # check for nonzero
                    ptr = new_ptr
                else:
                    ptr += 3

            elif opcode == '06':
                print(nstring)
                value_to_check = get_parameter_value_with_mode(ints, ptr, 1, nstring)
                new_ptr = get_parameter_value_with_mode(ints, ptr, 2, nstring)
                if value_to_check == 0:  # check for nonzero
                    ptr = new_ptr
                else:
                    ptr += 3

            elif opcode == '07':
                print(nstring)
                value_to_check = get_parameter_value_with_mode(ints, ptr, 1, nstring)
                x = value_to_check
                value_to_check = get_parameter_value_with_mode((ints, ptr, 2, nstring))
                y = value_to_check
                if x < y:
                    ints[ints[ptr + 3]] = 1
                else:
                    ints[ints[ptr + 3]] = 0
                ptr += 4

            elif opcode == '08':
                print(nstring)
                value_to_check = get_parameter_value_with_mode(ints, ptr, 1, nstring)
                x = value_to_check
                value_to_check = get_parameter_value_with_mode((ints, ptr, 2, nstring))
                y = value_to_check
                if x == y:
                    ints[ints[ptr + 3]] = 1
                else:
                    ints[ints[ptr + 3]] = 0
                ptr += 4

            else:
                print('unknown opcode ' + opcode)
                break



print(intcode([3,225,1,225,6,6,1100,1,238,225,104,0,1101,90,60,224,1001,224,-150,224,4,224,1002,223,8,223,1001,224,7,224,1,224,223,223,1,57,83,224,1001,224,-99,224,4,224,1002,223,8,223,1001,224,5,224,1,223,224,223,1102,92,88,225,101,41,187,224,1001,224,-82,224,4,224,1002,223,8,223,101,7,224,224,1,224,223,223,1101,7,20,225,1101,82,64,225,1002,183,42,224,101,-1554,224,224,4,224,102,8,223,223,1001,224,1,224,1,224,223,223,1102,70,30,224,101,-2100,224,224,4,224,102,8,223,223,101,1,224,224,1,224,223,223,2,87,214,224,1001,224,-2460,224,4,224,1002,223,8,223,101,7,224,224,1,223,224,223,102,36,180,224,1001,224,-1368,224,4,224,1002,223,8,223,1001,224,5,224,1,223,224,223,1102,50,38,225,1102,37,14,225,1101,41,20,225,1001,217,7,224,101,-25,224,224,4,224,1002,223,8,223,101,2,224,224,1,224,223,223,1101,7,30,225,1102,18,16,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,7,226,226,224,102,2,223,223,1006,224,329,101,1,223,223,1107,677,226,224,102,2,223,223,1006,224,344,1001,223,1,223,8,677,226,224,1002,223,2,223,1005,224,359,101,1,223,223,107,677,677,224,1002,223,2,223,1006,224,374,101,1,223,223,7,677,226,224,1002,223,2,223,1006,224,389,101,1,223,223,108,677,226,224,1002,223,2,223,1005,224,404,101,1,223,223,1108,677,226,224,102,2,223,223,1005,224,419,101,1,223,223,8,226,677,224,102,2,223,223,1006,224,434,1001,223,1,223,1008,677,677,224,1002,223,2,223,1005,224,449,1001,223,1,223,1107,226,677,224,102,2,223,223,1006,224,464,101,1,223,223,107,226,677,224,1002,223,2,223,1006,224,479,1001,223,1,223,7,226,677,224,102,2,223,223,1005,224,494,1001,223,1,223,8,677,677,224,102,2,223,223,1006,224,509,1001,223,1,223,1108,677,677,224,102,2,223,223,1005,224,524,1001,223,1,223,1108,226,677,224,1002,223,2,223,1005,224,539,101,1,223,223,107,226,226,224,102,2,223,223,1006,224,554,1001,223,1,223,1007,226,226,224,102,2,223,223,1005,224,569,1001,223,1,223,1008,226,226,224,102,2,223,223,1005,224,584,101,1,223,223,1007,677,677,224,1002,223,2,223,1005,224,599,1001,223,1,223,108,677,677,224,1002,223,2,223,1006,224,614,1001,223,1,223,1007,226,677,224,1002,223,2,223,1006,224,629,101,1,223,223,1008,677,226,224,102,2,223,223,1005,224,644,101,1,223,223,1107,226,226,224,1002,223,2,223,1005,224,659,1001,223,1,223,108,226,226,224,1002,223,2,223,1005,224,674,101,1,223,223,4,223,99,226]))
#print(intcode([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]))