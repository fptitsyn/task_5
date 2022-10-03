ans = []

for n in range(1, 1000):
    b = bin(n)
    b = b[2:]
    if b.count("1") % 2 == 0:
        b += "1"
    else:
        b += "0"
    if b.count("1") % 2 == 0:
        b += "1"
    else:
        b += "0"  
    
    r = int(b, 2)
    
    if 16 <= r <= 32:
        ans.append(r)
        
print(len(ans))