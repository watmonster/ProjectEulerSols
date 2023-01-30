isbroken = False

for a in range(1, 1000):
    for b in range(1, 1000):
        for c in range(1, 1000):
            if a+b+c == 1000:
                if a**2 + b**2 == c**2:
                    print("a: " + str(a))
                    print("b: " + str(b))
                    print("c: " + str(c))
                    print(a*b*c)
                    isbroken = True
                    break
        if isbroken == True:
            break
    if isbroken == True:
        break