import sys

t = int(sys.stdin.readline())
for q in range(t):
    a,b = map(int,sys.stdin.readline().split())

    c,d = a,b
    gcd = 0
    while True:
        if c > d:
            if c % d == 0:
                gcd = d
                break
            else:
                c,d = c%d,d

        else:
            if d % c == 0:
                gcd = c
                break
            else:
                d,c = c,d%c


    print(a*b//gcd)