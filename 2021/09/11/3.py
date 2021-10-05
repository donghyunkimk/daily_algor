def solution(fees, records):
    answer = []

    # 현재 자동차 상태(시간)
    car_info = dict()

    # 지금까지 누적 시간
    car_time = dict()

    # 자동차 23:59에 체크용
    car_check = []

    for q in records:
        a,b,c = q.split()
        if b not in car_info:
            car_info[b] = 0
            car_time[b] = 0
            car_check.append(b)

    for w in records:
        t, car, state = w.split()
        if car_info[car] == 0:
            car_info[car] = t

        else:
            car_time[car] += (int(t[:2]) - int(car_info[car][:2])) * 60 + int(t[3:]) - int(car_info[car][3:])
            car_info[car] = 0

    for e in car_check:
        if car_info[e] != 0:
            car_time[e] += 1439 - int(car_info[e][:2]) * 60 - int(car_info[e][3:])

    car_time = sorted(car_time.items(), key=lambda x:x[0])

    for r in car_time:
        rr,r = r
        i = r - fees[0]
        if i > 0:
            if i % fees[2] != 0:
                j = fees[1] + (i//fees[2]+1) * fees[3]

            else:
                j = fees[1] + (i//fees[2]) * fees[3]

            answer.append(j)

        else:
            answer.append(fees[1])

    answer = answer

    return answer

print(solution([180,5000,10,600],["05:34 5961 IN","06:00 0000 IN","06:34 0000 OUT","07:59 5961 OUT","07:59 0148 IN","18:59 0000 IN","19:09 0148 OUT","22:59 5961 IN","23:00 5961 OUT"]))
print(solution([120,0,60,591],["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1,461,1,10],["00:00 1234 IN"]))