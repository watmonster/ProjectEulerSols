palindrome = 0
isBroken = False

def is_palindrome(num):
    strnum = str(num)
    if len(strnum) == 5:
        if strnum[0] == strnum[4] and strnum[1] == strnum[3]:
            return True
    elif len(strnum) == 6:
        if strnum[0] == strnum[5] and strnum[1] == strnum[4] and strnum[2] == strnum[3]:
            return True
    return False

for i in range(999,400,-1):
    for j in range(999,400,-1):
        if is_palindrome(i*j):
            #print(i)
            #print(j)
            #palindrome = i*j
            print("Palindrome: " + str(i*j))
            if palindrome < i*j:
                palindrome = i*j
            #isBroken = True
            #break
        #else:
            #print("----------------------------")
            #print(i)
            #print(j)
            #print(i*j)
            #print("----------------------------")
    #if isBroken == True:
        #break

print("Biggest palindrome: " + str(palindrome))