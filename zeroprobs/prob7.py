def is_prime(num):
    div = 2
    while div <= num**(1/2):
        if num%div == 0:
            return False
        div += 1
    return True

numprimes = 0
currentnum = 2

while numprimes < 10002:
    if is_prime(currentnum):
        numprimes += 1
    if numprimes == 10001:
        print(currentnum)
        break
    currentnum += 1