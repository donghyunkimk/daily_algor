T = int(input())

for tc in range(1,1+T):

    # 수업 들어야하는 일수
    goal = int(input())

    # 시간표
    cal = list(map(int,input().split()))

    # 수업일수
    class_day = cal.count(1)

    # 필요한 수업일수가 1이 아닌 경우
    temp_num = 0
    if goal != 1:

        # goal - 1하는 이유
        # ex) goal이 2, class_day가 1인 경우
        # goal//class_day*7하면 14가 나옴
        # 이런 경우 제외하기 위해
        temp_num = (goal-1)//class_day*7
        if (goal-1)%class_day != 0:
            goal = 1 + (goal-1)%class_day
        else:
            goal = 1

    # 일 ~ 토를 시작일로 설정(idx)
    # 최소 날짜 구하기
    cnt = 9999999
    idx = 0
    while idx != 7:
        num = goal
        temp_cnt = 0
        for q in range(7):
            if cal[(q+idx)%7] == 1:
                num -= 1
            temp_cnt += 1
            if num == 0 or q == 6:
                idx += 1
                if temp_cnt < cnt:
                    cnt = temp_cnt
                break

    print('#{} {}'.format(tc,temp_num+cnt))