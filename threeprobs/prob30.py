sum = 0

def sum_fifth_power_digits(num):
    total = 0
    strnum = str(num)
    for char in strnum:
        total += (int(char))**5
    return total

for i in range(5000000):
    if i == sum_fifth_power_digits(i):
        print(i)
        sum += i
    if i%10000000 == 0:
        print("i currently at: " + str(i))

print(sum)