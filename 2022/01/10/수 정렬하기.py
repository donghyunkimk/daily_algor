n = int(input())

item = [0 for _ in range(2001)]

for q in range(n):
    item[abs(1000+int(input()))] = 1

for w in range(2001):
    if item[w] == 1:
        print(w-1000)