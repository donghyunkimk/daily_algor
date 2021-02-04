def bfs():
    temp = []
    temp.append([0,0,C])

    # 초기값 방문 확인
    visited[0][0][C] = 1

    while len(temp) != 0:

        # 첫 번째 물통 a, 두 번째 물통 b, 세 번째 물통 c
        a,b,c = temp.pop(0)

        # a가 0인 경우 중복을 피해서 c를 저장
        if a == 0:
            if c not in res:
                res.append(c)

        # a로 b,c를 채우는 경우
        if a != 0:

            # a로 b를 채우는 경우
            if b != B:

                # a에 있는 물의 양이 b의 빈 공간보다 큰 경우
                # B-b는 B에 넣을 수 있는 물의 양
                if B-b < a:
                    if visited[a-(B-b)][B][c] == 0:
                        temp.append([a-(B-b),B,c])
                        visited[a - (B - b)][B][c] = 1

                # a에 있는 물의 양이 b의 빈 공간 이하인 경우
                else:
                    if visited[0][a+b][c] == 0:
                        temp.append([0,a+b,c])
                        visited[0][a + b][c] = 1

            # a로 c를 채우는 경우
            if visited[0][b][a+c] == 0:
                temp.append([0,b,a+c])
                visited[0][b][a + c] = 1

        # b로 a,c를 채우는 경우
        if b != 0:

            # b로 a를 채우는 경우
            if a != A:

                if A-a < b:
                    if visited[A][b-(A-a)][c] == 0:
                        temp.append([A,b-(A-a),c])
                        visited[A][b - (A - a)][c] = 1

                else:
                    if visited[a+b][0][c] == 0:
                        temp.append([a+b,0,c])
                        visited[a + b][0][c] = 1

            # b로 c를 채우는 경우
            if visited[a][0][b+c] == 0:
                temp.append([a,0,b+c])
                visited[a][0][b + c] = 1

        # c로 a,b를 채우는 경우
        if c != 0:

            # c로 a를 채우는 경우
            if a != A:

                if A-a < c:
                    if visited[A][b][c-(A-a)] == 0:
                        temp.append([A,b,c-(A-a)])
                        visited[A][b][c - (A - a)] = 1

                else:
                    if visited[a+c][b][0] == 0:
                        temp.append([a+c,b,0])
                        visited[a + c][b][0] = 1

            # c로 b를 채우는 경우
            if b != B:

                if B-b < c:
                    if visited[a][B][c-(B-b)] == 0:
                        temp.append([a,B,c-(B-b)])
                        visited[a][B][c - (B - b)] = 1

                else:
                    if visited[a][b+c][0] == 0:
                        temp.append([a,b+c,0])
                        visited[a][b + c][0] = 1

    return



# 물통 A,B,C
A,B,C = map(int,input().split())

# 결과값
res = []

# 방문 여부 확인용
visited = [[[0]*(C+1) for _ in range(C+1)] for _ in range(C+1)]

bfs()

# 정렬
res.sort()

print(*res)