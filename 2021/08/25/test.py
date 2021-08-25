def solution(progresses, speeds):
    answer = []
    n = len(speeds)
    ans_lst = [0 for _ in range(n)]

    # 작업에 걸리는 시간 계산
    for q in range(n):
        if (100 - progresses[q]) / speeds[q] == (100 - progresses[q]) // speeds[q]:
            ans_lst[q] = (100 - progresses[q]) / speeds[q]

        else:
            ans_lst[q] = (100 - progresses[q]) // speeds[q] + 1

    cnt = 1
    num = ans_lst[0]

    # 현재 값보다 큰 값을 만날때까지 반복
    # 큰 값을 만나면 갱신
    for w in range(1, n):
        if num >= ans_lst[w]:
            cnt += 1

        else:
            answer.append(cnt)
            cnt = 1
            num = ans_lst[w]

        if w == n - 1:
            answer.append(cnt)

    return answer