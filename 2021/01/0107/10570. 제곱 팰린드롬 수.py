import sys
sys.stdin = open('10570. 제곱 팰린드롬 수.txt')

T = int(input())

for tc in range(1,1+T):
    a,b = map(int,input().split())

    # 제곱 팰린드롬 수의 갯수
    cnt = 0

    # 시작
    start = int(a**(1/2))

    # 끝
    end = int(b**(1/2))

    # 1,4,9 같은 경우 제외하기 위한 조건
    if start != a**(1/2):

        for q in range(start+1,end+1):
            if str(q**2)[0] == str(q**2)[-1] and str(q)[0] == str(q)[-1]:
                cnt += 1

    else:

        for q in range(start,end+1):
            if str(q**2)[0] == str(q**2)[-1] and str(q)[0] == str(q)[-1]:
                cnt += 1

    print('#{} {}'.format(tc,cnt))


    # for q in range(a,b+1):
    #     if q[0] == q[-1]: