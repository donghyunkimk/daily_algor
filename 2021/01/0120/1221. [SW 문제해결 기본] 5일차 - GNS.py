import sys
sys.stdin = open('1221. [SW 문제해결 기본] 5일차 - GNS.txt')

T = int(input())

# 정렬용 알파벳
number_alpha = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for tc in range(1,1+T):

    n = list(map(str,input().split()))

    # 무작위 숫자 리스트
    number_list = list(map(str,input().split()))

    # 결과 저장용
    res = []

    for q in range(10):
        for w in number_list:
            if number_alpha[q] == w:
                res.append(w)

    print(n[0])
    print(*res)