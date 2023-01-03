numbers = open('prob13text.txt','r')

sum = 0

for line in numbers:
    num = int(line)
    sum += num

print(sum)