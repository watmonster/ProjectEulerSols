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

def list_factors(num):
    factorlist = []
    for i in range(1, num//2+1):
        if num/i == num//i:
            factorlist.append(i)
    return factorlist

def sum_list(nums):
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
    return sum

def is_abundant(num):
    if sum_list(list_factors(num)) > num:
        return True
    else:
        return False

abundants = set()

for k in range(28124):
    if is_abundant(k):
        abundants.add(k)
        print(k)

def is_sum_abundant(num):
    for j in range(1,num//2 + 2):
        if j in abundants and num-j in abundants:
            return True
    return False

sumints = 0

for l in range(1, 49):
    if not is_sum_abundant(l):
        print(l)
        sumints += l

for m in range(49, 28124, 2):
    #print(m)
    if not is_sum_abundant(m):
        print(m)
        sumints += m

print(sumints)