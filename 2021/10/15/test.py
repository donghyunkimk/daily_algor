fibo = [[1,0],[0,1]]

for q in range(2,41):
    i,j = fibo[q-2]
    ii,jj = fibo[q-1]

    fibo.append([i+ii,j+jj])

T = int(input())

for tc in range(1,1+T):
    n = int(input())

    print(*fibo[n])
