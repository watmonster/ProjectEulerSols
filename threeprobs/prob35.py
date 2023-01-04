def is_prime(num):
    div = 2
    while div <= num**(1/2):
        if num%div == 0:
            return False
        div += 1
    return True

def shift(num, amt):
    if amt == 0:
        return num
    strnum = str(num)
    first = strnum[:amt]
    second = strnum[amt:]
    newnum = second+first
    return int(newnum)

cps = []

def is_circular_prime(num):
    strnum = str(num)
    isanyeven = False
    for char in strnum:
        if int(char)%2 == 0:
            isanyeven = True
    if isanyeven == True:
        return False
    icp = True
    for i in range(len(strnum)):
        if not is_prime(shift(num, i)):
            icp = False
    return icp

for j in range(1, 1000000, 2):
    if is_circular_prime(j):
        cps.append(j)
        print(j)

print(cps)
print(len(cps))