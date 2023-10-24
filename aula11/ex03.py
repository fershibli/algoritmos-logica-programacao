primos = []
n = 100

while len(primos) < 10:
    primo = True
    for k in range(2, n//2):
        if (n % k) == 0:
            primo = False
            break
    if primo:
        primos.append(n)
    n = n + 1

t = tuple(primos)

for x in range(len(t)):
    print(t[x])