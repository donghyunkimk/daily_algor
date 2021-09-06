def solution(weights, head2head):
    n = len(weights)
    rank = [0 for _ in range(n)]

    for q in range(n):

        # 승, 패, 더 무거운 복서 이긴 횟수
        win = 0
        lose = 0
        win_more = 0
        while True:
            for w in range(n):
                if head2head[q][w] == 'W':
                    win += 1
                    if weights[q] < weights[w]:
                        win_more += 1

                elif head2head[q][w] == 'L':
                    lose += 1

            if win == 0 and lose == 0:

                # 승률, 더 무거운 복서 이긴 횟수, 몸무게, 번호
                rank[q] = [0, 0, weights[q], q + 1]

            else:
                rank[q] = [win / (win + lose), win_more, weights[q], q + 1]

            break

    # 번호는 내림차순이므로 정렬할 필요 없음
    rank.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)

    answer = [0 for _ in range(n)]
    for w in range(n):
        answer[w] = rank[w][3]

    return answer

# 알아야하는 것
# 승률, 자신보다 무거운 복서 이긴 횟수, 몸무게, 복서의 번호
# 다른 복서랑 전적 없는 경우 = 0퍼센트

# 승률 높은 순서
# 몸무게 무거운 복서 많이 이긴 횟수
# 몸무게 무거운 순서
# 작은 번호