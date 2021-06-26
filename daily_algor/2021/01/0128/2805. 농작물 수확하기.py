import sys
sys.stdin = open('2805. 농작물 수확하기.txt')

T = int(input())

for tc in range(1,1+T):

    # 농장의 크기
    n = int(input())

    # 농장
    farm = [list(map(int,input())) for _ in range(n)]

    # 결과
    res = 0

    # 3가지 경우의 수
    # 1. 0~n//2까지
    for case1_i in range(0,n//2):
        for case1_j in range(case1_i+1):
            if case1_j == 0:
                res += farm[case1_i][n//2]

            else:
                res += farm[case1_i][n//2+case1_j]
                res += farm[case1_i][n//2-case1_j]

    # 2. n//2
    for case2_j in range(n):
        res += farm[n//2][case2_j]

    # 3. n//2+1 ~ n까지
    for case3_i in range(n//2+1,n):
        for case3_j in range(n-case3_i):
            if case3_j == 0:
                res += farm[case3_i][n//2]

            else:
                res += farm[case3_i][n//2+case3_j]
                res += farm[case3_i][n//2-case3_j]

    print('#{} {}'.format(tc,res))