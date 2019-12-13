import re
from collections import Counter

def password(input):
    nums = [int(n) for n in input.split("-")]
    passwords = []
    validpasswords = []
    parttwopasswords = []
    validflag = True
    for n in range(nums[0], nums[1]):
        passwords.append(str(n))  
    for password in passwords:
        if re.search(r'(.)\1+', password):
            for i, c in enumerate(password):
                if int(c) < int(password[i - 1]) and i > 0:
                    validflag = False
            if validflag:
                validpasswords.append(password)
        validflag = True
    print(len(validpasswords))
# Part 2
    for password in validpasswords:
        c = Counter(password)
        if 2 in c.values():
            parttwopasswords.append(password)
    print(len(parttwopasswords))

password("165432-707912")