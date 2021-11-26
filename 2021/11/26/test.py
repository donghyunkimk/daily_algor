n,k = map(int,input().split())

ans = []

for q in range(1,int(n**(1/2))+1):
    if n % q == 0:
        if q**2 != n:
            ans.append(q)
            ans.append(n//q)
        else:
            ans.append(q)

if k > len(ans):
    print(0)
else:
    ans.sort()
    print(ans[k-1])