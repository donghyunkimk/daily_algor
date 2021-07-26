import sys
sys.stdin = open('3408. 세가지 합 구하기.txt')

# 통과 코드
T = int(input())

n = [int(input()) for _ in range(T)]

for q in range(T):
    s2 = n[q]**2
    s3 = n[q]**2+n[q]
    if n[q]%2 == 0:
        s1 = (n[q]+1)*(n[q]//2)
        print('#{} {} {} {}'.format(q + 1, s1, s2, s3))

    else:
        s1 = (n[q] + 1) * (n[q] // 2) + (n[q] + 1) // 2
        print('#{} {} {} {}'.format(q+1,s1,s2,s3))

# 시간 초과 코드
T = int(input())

for tc in range(1,1+T):
    N = int(input())

    S1 = 0
    for q in range(1,N+1):
        S1 += q
    S2 = N**2
    S3 = S2+N

    print('#{} {} {} {}'.format(tc,S1,S2,S3))

T = int(input())

for tc in range(1, 1 + T):
    n = int(input())
    s2 = n ** 2
    s3 = n ** 2 + n
    if n % 2 == 0:
        s1 = (n + 1) * (n // 2)
        print('#{} {} {} {}'.format(tc, s1, s2, s3))
    else:
        s1 = (n+1)*(n//2) + (n+1)//2
        print('#{} {} {} {}'.format(tc, s1, s2, s3))

