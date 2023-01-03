def is_prime(num):
    div = 2
    while div <= num**(1/2):
        if num%div == 0:
            return False
        div += 1
    return True

def listPrimeFactors(num):
    pfs = []
    currentDivisor = 2
    while num > 1:
        divisorCount = 0
        while num%currentDivisor == 0:
            num = num // currentDivisor
            divisorCount += 1
        if divisorCount > 0:
            for i in range(divisorCount):
                pfs.append(currentDivisor)
        currentDivisor += 1
        while not is_prime(currentDivisor):
            currentDivisor += 1
    return pfs

print(listPrimeFactors(600851475143))