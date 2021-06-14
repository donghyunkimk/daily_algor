# 2016년의 달력
calendar = [_ for _ in range(12)]

for q in range(1,13):

    # 30일 - 4,6,9,11
    if q == 4 or q == 6 or q == 9 or q == 11:
        calendar[q-1] = [0 for _ in range(30)]

    # 29일 - 2
    elif q == 2:
        calendar[q-1] = [0 for _ in range(29)]

    # 31일 - 1,3,5,7,8,10,12
    else:
        calendar[q-1] = [0 for _ in range(31)]

# 요일, 1.1은 금요일(4)
day = 4

# 날짜 채우기
for w in range(12):
    for e in range(len(calendar[w])):

        # 요일 - 월 0 화 1 수 2 목 3 금 4 토 5 일 6
        # 일주일은 7일이므로 7로 나눴을 때의 나머지를 이용
        calendar[w][e] = day%7
        day += 1

T = int(input())

for tc in range(1,1+T):

    # 월, 일
    m,d = map(int,input().split())

    print('#{} {}'.format(tc,calendar[m-1][d-1]))