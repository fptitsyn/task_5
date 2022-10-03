c = 0

for x in range(100, 1000):
    a1 = x // 10**2 % 10
    a2 = x // 10 % 10
    a3 = x % 10
    if (a1 + a2 == 12 and a2 + a3 == 16) or (a1 + a2 == 16 and a2 + a3 == 12):
        c += 1
        
print(c)