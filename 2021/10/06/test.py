def find(idx,cur_sum):
    global goal

    # 원하는 값 찾았을 때
    # s가 0인 예외 케이스 제거하기 위해 idx != 0 조건 추가
    if cur_sum == s and idx != 0:
        if idx == n:
            goal += 1
            return

        # 끝까지 돌려서 s 되는 모든 경우 찾기 위해
        # ex) s = 0, board = -1 1 3 -3 인 경우
        # 해당 조건 없이 return하면 1에서 끝남, 근데 -1 1 3 -3 도 s를 만족 함
        else:
            goal += 1

    for q in range(idx,n):
        find(q+1,cur_sum+board[q])

    return

n,s = map(int,input().split())

board = list(map(int,input().split()))

goal = 0

find(0,0)

print(goal)