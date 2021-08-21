def solution(dartResult):
    answer = 0
    score = [0, 0, 0]
    check = [0 for _ in range(len(dartResult))]
    idx = 0
    for q in range(len(dartResult)):
        if idx < 3:
            if 48 <= ord(dartResult[q]) <= 57:
                if 48 <= ord(dartResult[q + 1]) <= 57:
                    if dartResult[q + 2] == 'S':
                        score[idx] = 10

                    elif dartResult[q + 2] == 'D':
                        score[idx] = 100

                    else:
                        score[idx] = 1000

                else:

                    if dartResult[q + 1] == 'S':
                        score[idx] = int(dartResult[q])

                    elif dartResult[q + 1] == 'D':
                        score[idx] = int(dartResult[q]) ** 2

                    else:
                        score[idx] = int(dartResult[q]) ** 3

                idx += 1

    idx = 2

    for w in range(-1,-len(dartResult)-1,-1):
        if idx > 0:
            if dartResult[w] == '*':
                score[idx] *= 2
                score[idx-1] *= 2
                idx -= 1

            elif dartResult[w] == '#':
                score[idx] *= -1
                score[idx-1] *= -1
                idx -= 1

        else:
            if dartResult[w] == '*':
                score[idx] *= 2

            elif dartResult[w] == '#':
                score[idx] *= -1

    answer = score

    return answer

print(solution('1D2S#10S'))