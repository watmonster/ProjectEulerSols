def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n*factorial(n-1)

def choose(n,r):
    return (factorial(n)//(factorial(r)*factorial(n-r)))

values = []

for n in range(1,101):
    for r in range(n):
        if choose(n,r) > 1000000:
            values.append(choose(n,r))

print(len(values))