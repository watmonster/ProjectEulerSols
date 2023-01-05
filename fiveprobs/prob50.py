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

