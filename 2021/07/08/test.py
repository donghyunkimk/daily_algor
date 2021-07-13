def solution(scoville, K):
    answer = 0

    scoville.sort()

    if scoville[0] < K:
        temp_answer = scoville[0] + scoville[1] * 2
        answer += 1
        idx = 2

        while True:
            temp_num













    return answer