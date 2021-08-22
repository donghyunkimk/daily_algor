def solution(n, arr1, arr2):
    lst = [[0 for _ in range(n)] for l in range(n)]

    # 벽 lst에 표시
    idx = 0
    for q in arr1:
        num = format(q, 'b')
        num_lst = list(str(num))

        for qq in range(-1, -len(num_lst) - 1, -1):
            if int(num_lst[qq]) == 1:
                lst[idx][qq] += 1

        idx += 1

    idx = 0
    for q in arr2:
        num = format(q, 'b')
        num_lst = list(str(num))

        for qq in range(-1, -len(num_lst) - 1, -1):
            if int(num_lst[qq]) == 1:
                lst[idx][qq] += 1

        idx += 1

    # 벽 있는 인덱스는 #으로 표시
    answer = [0 for _ in range(n)]
    for w in range(n):
        temp = ''
        for e in range(n):
            if lst[w][e] != 0:
                temp += '#'

            else:
                temp += ' '
        answer[w] = temp

    return answer