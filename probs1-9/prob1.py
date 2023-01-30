sum = 0

for i in range(1000):
    if i/3 == i//3:
        sum += i
    if i/5 == i//5:
        sum += i
    if i/15 == i//15:
        sum -= i

print(sum)
