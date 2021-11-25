n = int(input())

ans = []
for q in range(n):
    a,b = map(str,input().split())

    ans.append([q,int(a),b])

ans.sort(key=lambda x:(x[1],x[0]))

for w in ans:
    print(*w[1:])