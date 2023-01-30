def compute_prime_factorization(num):
    '''compute_prime_factorization(num) -> dict
    returns a dictionary with the prime factorization of num'''
    primes = {} # keep track of the primes
    divisor = 2 # keep track of the divisor
    while num > 1:
        divisorCount = 0  # keeps track of how many times we can divide divisor into num
        while num % divisor == 0:  # divisor is a factor
            num = num // divisor
            divisorCount += 1
        if divisorCount > 0:   # if we had any, add a dict entry
            primes[divisor] = divisorCount
        divisor += 1  # increment the divisor
    return primes

def num_factors(num):
    '''num_factors(num) -> int
    returns the number of factors of num'''
    # get prime factorization
    primes = compute_prime_factorization(num)
    # get product of exponents+1
    numFactors = 1
    for prime in primes:
        numFactors *= primes[prime]+1
    return numFactors

def nthtriangle(n):
    return (n * (n+1))/2

currentnum = 1
currenttrianglenum = nthtriangle(currentnum)
ctnfactors = num_factors(currenttrianglenum)

while ctnfactors <= 500:
    currentnum += 1
    currenttrianglenum = nthtriangle(currentnum)
    ctnfactors = num_factors(currenttrianglenum)
    if ctnfactors > 500:
        print(currentnum)
        print(currenttrianglenum)
        print(ctnfactors)
