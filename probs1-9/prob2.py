sumEvenFib = 0


def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return fib(n-1)+fib(n-2)


currentFibNum = 1
currentFib = fib(1)

while currentFib < 4000000:
    if currentFib/2 == currentFib//2:
        sumEvenFib += currentFib
        print(currentFib)
    currentFibNum += 1
    currentFib = fib(currentFibNum)

print(sumEvenFib)
