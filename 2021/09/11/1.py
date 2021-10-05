def solution(id_list, report, k):
    answer = []

    id_dict = dict()

    # check = [0 for _ in range(len(id_list))]
    check = dict()

    for q in id_list:
        id_dict[q] = []
        check[q] = 0

    for w in report:
        a,b = w.split()
        if b not in id_dict[a]:
            id_dict[a].append(b)
            check[b] += 1

    for e in id_dict:
        temp = id_dict[e]
        cnt = 0
        for ee in temp:
            if check[ee] >= k:
                cnt += 1

        answer.append(cnt)


    return answer

print(solution(	["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))