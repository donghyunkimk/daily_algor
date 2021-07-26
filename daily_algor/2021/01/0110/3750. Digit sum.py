import sys
sys.stdin = open('3750. Digit sum.txt')

T = int(input())

for tc in range(1,1+T):
    n = str(input())

    while len(n) > 1:
        res = 0
        for q in n:
            res += int(q)
        n = str(res)

    print('#{} {}'.format(tc,n))

def dfs(num):
    global res
    # 탈출조건, 한 자리 숫자일 때
    if len(num) == 1:

        # res에 현재 값 저장
        res = num
        return

    temp = 0
    for w in num:
        temp += int(w)

    dfs(str(temp))

    return

T = int(input())

n = [str(input()) for _ in range(T)]

for q in range(T):
    res = 0
    dfs(n[q])

    print('#{} {}'.format(q+1,res))