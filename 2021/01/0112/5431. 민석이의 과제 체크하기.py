import sys
sys.stdin = open('5431. 민석이의 과제 체크하기.txt')

T = int(input())

for tc in range(1,1+T):

    # n 수강생 수, k 제출한 사람 수
    n,k = map(int,input().split())

    # 제출한 사람의 번호
    submitted = list(map(int,input().split()))

    # 제출 안 한 사람 저장소
    no_submitted = []

    for q in range(1,n+1):
        if q not in submitted:
            no_submitted.append(q)

    print('#{}'.format(tc),*no_submitted)