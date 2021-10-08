def find(idx,start):
    global res

    # 스타트 팀이 다 채워졌으면
    if len(start) == n//2:

        # 링크 팀 채우기
        link = []
        for e in range(n):
            if e not in start:
                link.append(e)

        # 능력치 합계
        start_score = 0
        for r in range(n//2):
            for rr in range(n//2):
                start_score += board[start[r]][start[rr]]

        link_score = 0
        for t in range(n//2):
            for tt in range(n//2):
                link_score += board[link[t]][link[tt]]

        if abs(start_score-link_score) < res:
            res = abs(start_score-link_score)

        return

    for w in range(idx,n):
        find(w+1,start+[w])

    return

n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]

res = 50000

for q in range(n//2+1):
    # 처음 값을 추가
    find(q+1,[q])

print(res)