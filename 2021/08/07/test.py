def solution(dartResult):

    # 점수
    score = [0,0,0]

    # 점수 인덱스
    idx = 0

    # 방문 확인
    check = [0 for _ in range(len(dartResult))]

    # 기본 점수 확인
    for q in range(len(dartResult)):
        if check[q] == 0:

            # '0' <= dartResult[q] <= '9' 이면
            if 48 <= ord(dartResult[q]) <= 57:
                check[q] = 1

                # 10인 경우
                if 48 <= ord(dartResult[q+1]) <= 57:
                    check[q+1] = 1
                    if dartResult[q+2] == 'S':
                        score[idx] = 10

                    elif dartResult[q+2] == 'D':
                        score[idx] = 100

                    else:
                        score[idx] = 1000

                # 10이 아닌 경우
                else:
                    if dartResult[q + 1] == 'S':
                        score[idx] = int(dartResult[q])

                    elif dartResult[q + 1] == 'D':
                        score[idx] = int(dartResult[q]) ** 2

                    else:
                        score[idx] = int(dartResult[q]) ** 3

                idx += 1

    # 보너스 계산하기
    for w in range(len(dartResult)):
        if dartResult[w] == '*':
            if w == 2:
                score[0] *= 2

            elif w == 4 or w == 5:
                score[0] *= 2
                score[1] *= 2

            else:
                score[1] *= 2
                score[2] *= 2

        elif dartResult[w] == '#':
            if w == 2:
                score[0] *= -1

            elif w == 4 or w == 5:
                score[1] *= -1

            else:
                score[2] *= -1

    answer = sum(score)

    return answer