ans = []
for n in range(10, 100):
    if (n % 4 == 1) and (n % 2 == 1) and (n % 3 == 2):
        ans.append(n)
        
print(min(ans))