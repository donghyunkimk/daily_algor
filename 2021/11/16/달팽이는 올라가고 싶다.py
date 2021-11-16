a,b,v = map(int,input().split())

my_v = v - a
day = my_v // (a-b)
hei = day * (a-b)
while True:
    day += 1
    hei += a
    if hei >= v:
        break

    else:
        hei -= b

print(day)