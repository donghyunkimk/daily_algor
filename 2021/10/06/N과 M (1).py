def find(cnt,word):
    if cnt == m:

        answer.append(word)

        return

    for w in range(1,n+1):
        if check[w] == 0:
            check[w] = 1
            find(cnt+1,word+[w])
            check[w] = 0

    return

n,m = map(int,input().split())

answer = []

for q in range(1,n+1):
    check = [0 for _ in range(n+1)]
    check[q] = 1
    find(1,[q])

for e in answer:
    for r in e:
        if e[-1] != r:
            print(r,end=' ')

        else:
            print(r)