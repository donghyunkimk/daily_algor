a,b = map(int,input().split())

c,d = a,b
gcd = 0
while True:
    if c > d:
        if c % d == 0:
            gcd = d
            break
        else:
            c,d = d,c%d

    else:
        if d % c == 0:
            gcd = c
            break
        else:
            d,c = d%c,c

print(gcd)
print(a*b//gcd)