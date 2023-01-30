def is_prime(num):
    div = 2
    while div <= num**(1/2):
        if num%div == 0:
            return False
        div += 1
    return True

def is_permutation(num, num2):
    strnum = str(num)
    setnum = set()
    for char in strnum:
        setnum.add(char)
    strnum2 = str(num2)
    setnum2 = set()
    for char2 in strnum2:
        setnum2.add(char2)
    if setnum == setnum2:
        return True
    else:
        return False

for i in range(1001,3340, 2):
    if is_prime(i):
        if is_prime(i+3330):
            if is_prime(i+6660):
                if is_permutation(i, i+3330):
                    if is_permutation(i, i+6660):
                        if is_permutation(i+3330, i+6660):
                            print(i)
                            print(i+3330)
                            print(i+6660)



#3340