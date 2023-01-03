def sum_digits(num):
    strnum = str(num)
    total = 0
    for char in strnum:
        total += int(char)
    return total

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

print(sum_digits(factorial(100)))