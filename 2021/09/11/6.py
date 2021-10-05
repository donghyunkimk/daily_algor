def solution(board, skill):
    answer = len(board)*len(board[0])

    for q in skill:
        type, i, j, ii, jj, power = q

        for w in range(i,ii+1):
            for e in range(j,jj+1):
                if type == 1:
                    if board[w][e] > 0 and board[w][e] - power <= 0:
                        answer -= 1

                    board[w][e] -= power

                else:
                    if board[w][e] <= 0 and board[w][e] + power > 0:
                        answer += 1

                    board[w][e] += power

    return answer

print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))
print(solution([[1,2,3],[4,5,6],[7,8,9]],[[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))
# board = 건물
# skill[0], 1 = 공격, 2 = 회복
# skill[1~4], [skill[1],skill[2]] ~ [skill[3],skill[4]]
# skill[5], 효과