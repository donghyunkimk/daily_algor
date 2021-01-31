import sys
sys.stdin = open('4012. [모의 SW 역량테스트] 요리사.txt')


def comb(cnt,idx,start):
    if cnt == find_num:
        cal(0)
        return

    else:
        for q in range(start,n):
            p1[idx] = q
            comb(cnt+1,idx+1,q+1)
    return


def cal(p2_cnt):
    global min_res
    customer1 = 0
    customer2 = 0


    for w in range(n):
        if w not in p1:
            p2[p2_cnt] = w
            p2_cnt += 1

    for i in range(n//2):
        for j in range(n//2):
            if i != j:
                customer1 += foods[p1[i]][p1[j]]
                customer2 += foods[p2[i]][p2[j]]

    if abs(customer1 - customer2) < min_res:
        min_res = abs(customer1 - customer2)

    return

T = int(input())

for tc in range(1,1+T):
    n = int(input())

    foods = [list(map(int,input().split())) for _ in range(n)]

    min_res = 20000 * n

    p1 = [0]*(n//2)
    p2 = [0]*(n//2)

    find_num = n//2

    comb(0,0,0)

    print('#{} {}'.format(tc, min_res))