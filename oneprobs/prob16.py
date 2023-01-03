def sum_digits(num):
    strnum = str(num)
    total = 0
    for char in strnum:
        total += int(char)
    return total

print(sum_digits(2**1000))