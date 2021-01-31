import sys
sys.stdin = open('2386. [AtCoder Beginner Contest 073] C. Write and Erase.txt')

T = int(input())

for tc in range(1,1+T):

    # Joisino가 n번 부름
    n = int(input())

    # 저장 위치
    res = []

    for q in range(n):

        # Joisino가 부르는 숫자
        temp = int(input())

        # 중복되지 않으면
        if temp not in res:

            # 저장
            res.append(temp)

        # 중복되면
        else:

            # 해당 숫자 제거
            res.remove(temp)

    print('#{} {}'.format(tc,len(res)))