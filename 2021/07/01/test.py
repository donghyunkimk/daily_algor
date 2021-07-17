def solution(citations):
    answer = 0

    citations.sort()

    num = len(citations)

    for q in range(num):

        if min(num - q, citations[q]) > answer:
            answer = min(num - q, citations[q])

    return answer