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

for i in range(100000000):
    if is_permutation(i, 2*i) and is_permutation(i,3*i) and is_permutation(i,4*i) and is_permutation(i,5*i) and is_permutation(i,6*i):
        print(i)