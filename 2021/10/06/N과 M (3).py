def find(cnt,word):
    if cnt == m:

        answer.append(word)

        return

    for w in range(1,n+1):
        find(cnt+1,word+[w])

    return

n,m = map(int,input().split())

answer = []

for q in range(1,n+1):
    find(1,[q])

for e in answer:
    print(*e)