sum = 0

facs = [1,1,2,6,24,120,720,5040,40320,362880]

def sum_factorial_digits(num):
    total = 0
    strnum = str(num)
    for char in strnum:
        total += facs[int(char)]
    return total

for i in range(5000000):
    if i == sum_factorial_digits(i):
        print(i)
        sum += i
    if i%1000000 == 0:
        print("i currently at: " + str(i))

print(sum-3)