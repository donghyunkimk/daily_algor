import sys
sys.stdin = open('비상구 탈출.txt')

def dfs(idx,fir_time,sec_time):
    if fir_time == goal_lst[idx][0]:
        dfs(idx+1,fir_time+1,sec_time)
    elif fir_time < goal_lst[idx][0]:
        dfs(idx+1,goal_lst[idx][0],sec_time)
    else:
        dfs(idx+1,fir_time,sec_time)

    if sec_time == goal_lst[idx][1]:
        dfs(idx + 1, fir_time, sec_time + 1)
    elif sec_time < goal_lst[idx][1]:
        dfs(idx + 1,fir_time , goal_lst[idx][1])
    else:
        dfs(idx + 1, fir_time, sec_time)

    return [fir_time, sec_time]

T = int(input())

for tc in range(1,1+T):

    N = int(input())

    board = [list(map(int,input().split())) for _ in range(N)]

    goal = []
    goal_sec = []
    people = []

    for q in range(N):
        for w in range(N):
            if board[q][w] == 2:
                if len(goal) == 0:
                    goal.append(q)
                    goal.append(w)

                else:
                    goal_sec.append(q)
                    goal_sec.append(w)

            elif board[q][w] == 1:
                people.append([q,w])

    goal_lst = []
    goal_sec_lst = []

    for e in range(len(people)):
        temp1 = abs(people[e][0]-goal[0]) + abs(people[e][1]-goal[1])
        temp2 = abs(people[e][0]-goal_sec[0]) + abs(people[e][1]-goal_sec[1])

        goal_lst.append([temp1,temp2,e])

    visited = [0]*len(people)

    goal_lst.sort(key=lambda x:[x[0],x[1]])

    time = 0

    res = dfs(0,0,0)

    print(res[0],res[1])