fibs = [0,1,1]

for i in range(3,10001):
    fibs.append(fibs[i-1]+fibs[i-2])
    if i%100 == 0:
        print(i)
        print(fibs[i])

def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def num_fib_digits(n):
    fibn = fibs[n]
    strfibn = str(fibn)
    return len(strfibn)

indexOfFib = 1
nfdiof = num_fib_digits(indexOfFib)

while nfdiof < 1000:
    indexOfFib += 1
    nfdiof = num_fib_digits(indexOfFib)
    print(nfdiof)
    if nfdiof == 1000:
        print(indexOfFib)