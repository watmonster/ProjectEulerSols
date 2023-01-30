def is_prime(num):
    div = 2
    while div <= num**(1/2):
        if num%div == 0:
            return False
        div += 1
    return True

sumPrimes = 0

for i in range(2, 2000000):
    if is_prime(i):
        sumPrimes += i

print(sumPrimes)