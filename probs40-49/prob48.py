total = 0

for i in range(1,1001):
    total += i**i

strtotal = str(total)
print(strtotal[-10:])