T = int(input())

for tc in range(1,1+T):

    # 정점의 개수, 간선의 개수
    v,e = map(int,input().split())

    # 간선의 정보
    board = [list(map(int,input().split())) for _ in range(e)]

    # 사이클 막기 위한 방문용
    visited = [0 for _ in range(v+1)]

    # 간선의 정보 저장
    line_info = [[] for _ in range(v+1)]

    for line in board:
        line_info[line[0]].append([line[1],line[2]])
        line_info[line[1]].append([line[0],line[2]])
        # line_info[line[0]].append(line[1])
        # line_info[line[0]].append(line[2])
        # line_info[line[1]].append(line[0])
        # line_info[line[1]].append(line[2])


    res = 0
    visited[1] = 1
    temp = line_info[1][:]
    temp.sort(key=lambda x : x[1])

    while True:
        for q in range(len(temp)):
            if visited[temp[q][0]] == 0:
                visited[temp[q][0]] = 1
                res += temp[q][1]
                temp.extend(line_info[temp[q][0]])
                break

        del temp[q:q+1]
        temp.sort(key=lambda x : x[1])

        if visited.count(0) == 1:
            break

    print('#{} {}'.format(tc,res))