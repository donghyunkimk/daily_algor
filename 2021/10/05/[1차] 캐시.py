def solution(cacheSize, cities):
    answer = 0

    answer_lst = []

    # 0인 경우(예외 케이스)
    if cacheSize == 0:
        answer = len(cities) * 5

    else:

        # cities를 돌면서 answer_lst 안에 값이 없으면 추가
        # 존재하면 해당 값을 제거한 후, 마지막 위치에 값 추가
        for q in cities:
            if q not in answer_lst:
                if len(answer_lst) < cacheSize:
                    answer_lst.append(q)
                    answer += 5

                else:
                    answer_lst.pop(0)
                    answer_lst.append(q)
                    answer += 5

            else:
                answer_lst.pop(answer_lst.index(q))
                answer_lst.append(q)
                answer += 1

    return answer

print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))