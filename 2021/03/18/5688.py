# 세제곱수를 저장할 공간
num = [0]*(10**6+1)

# num[세제곱근]에 세제곱수를 저장
for q in range(1,10**6+1):
    num[q] = q**3

T = int(input())

for tc in range(1,1+T):
    n = int(input())

    # .index를 사용해서 n을 탐색할 때,
    # n이 num 안에 존재하지 않으면 오류 발생(n is not in list 오류)
    # 이를 해결하기 위해 예외처리로 문제 해결
    try:
        print('#{} {}'.format(tc,num.index(n)))

    except:
        print('#{} {}'.format(tc,-1))