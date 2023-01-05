def reverse(num):
    strnum = str(num)
    reversednum = ""
    for i in range(len(strnum)):
        reversednum += strnum[len(strnum)-(i+1)]
    return int(reversednum)

def reverse_add(num):
    return num + reverse(num)

def is_palindrome(num):
    strnum = str(num)
    ispal = True
    for j in range(len(strnum)//2 + 1):
        if strnum[j] != strnum[len(strnum)-(j+1)]:
            ispal = False
    return ispal

lychrels = []

for k in range(10000):
    isLychrel = True
    m = k
    for l in range(50):
        m = reverse_add(m)
        if is_palindrome(m):
            isLychrel = False
            break
    if isLychrel == True:
        lychrels.append(k)

print(len(lychrels))