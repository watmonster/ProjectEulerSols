success = False
num = 1

while success == False:
    if num%16 == 0 and num%9 == 0 and num%5 == 0 and num%7 == 0 and num%11 == 0 and num%13 == 0 and num%17 == 0 and num%19 == 0:
        print(num)
        success = True
    else:
        num += 1