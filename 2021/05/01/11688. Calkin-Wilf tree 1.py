T = int(input())

# 연산속도를 높이기 위해 만든 res
# append로 배열에 값을 추가하면 속도가 느림
# 미리 10000개의 빈 배열을 만들어 놓고
# 10000개의 결과 값을 저장
res = [[0,0] for _ in range(T+1)]

for tc in range(1,1+T):

    # 방향
    dir = list(input())

    # a,b의 초기 값
    a = 1
    b = 1

    # for문 돌면서 a,b 값 수정
    for q in dir:
        if q == 'L':
            b = a+b

        else:
            a = a+b
            b = b

    # res에 저장
    res[tc][0] = a
    res[tc][1] = b

for res_tc in range(1,1+T):
    print('#{} {} {}'.format(res_tc,res[res_tc][0],res[res_tc][1]))