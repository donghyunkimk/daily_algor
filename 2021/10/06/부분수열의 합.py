def find(idx,cnt,cur_sum):
    global goal

    if cnt == q+1 or idx == n:
        if cur_sum == s and cnt == q+1:
            goal += 1
        return

    for w in range(idx,n):

        find(w+1,cnt+1,cur_sum+board[w])

    return

n,s = map(int,input().split())

board = list(map(int,input().split()))

goal = 0

for q in range(n):
    find(0,0,0)

print(goal)