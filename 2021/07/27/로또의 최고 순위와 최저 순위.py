def solution(lottos, win_nums):
    answer = []

    cnt = 0
    for q in win_nums:
        for w in lottos:
            if q == w:
                cnt += 1
                break

    zero_cnt = lottos.count(0)

    low = 7 - cnt
    high = 7 - cnt - zero_cnt
    if cnt == 0:
        low = 6
        if zero_cnt == 0:
            high -= 1

    answer = [high, low]

    return answer


def solution(lottos, win_nums):
    answer = []

    score = [6,6,5,4,3,2,1]

    zero_cnt = lottos.count(0)

    cnt = 0
    for q in win_nums:
        for w in lottos:
            if q == w:
                cnt += 1
                break

    answer = [score[zero_cnt+cnt], score[cnt]]

    return answer