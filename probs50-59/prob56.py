def sum_digits(num):
    sum = 0
    strnum = str(num)
    for char in strnum:
        sum += int(char)
    return sum

maxsum = 0

for a in range(100):
    for b in range(100):
        if sum_digits(a**b) > maxsum:
            maxsum = sum_digits(a**b)

print(maxsum)