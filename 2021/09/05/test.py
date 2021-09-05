# def solution(N, stages):
#     answer = [0 for _ in range(N)]
#     # 유저수
#     u = len(stages)
#
#     stages.sort(reverse=True)
#     # 클리어 못한 유저수
#     # 해당 스테이지에서 막힌 유저수, 해당 스테이지에 도달한 유저수, 스테이지 번호
#     unclear = [[0,0,_] for _ in range(N)]
#
#     cnt = 0
#     for q in stages:
#         cnt += 1
#
#         if q != N + 1:
#             unclear[q-1][0] += 1
#             unclear[q-1][1] = cnt
#
#     # 실패율, 스테이지 번호
#     u_info = [[0,_+1] for _ in range(N)]
#     for w in unclear:
#         if w[0] != 0 and w[1] != 0:
#             u_info[w[2]][0] = w[0] / w[1]
#         else:
#             u_info[w[2]][0] = 0
#
#     u_info.sort(key=lambda x:x[0], reverse=True)
#
#     # 실패율
#     for e in range(N):
#         answer[e] = u_info[e][1]
#
#     return answer
#
# print(solution(4,[4,4,4,4,4]))
# # 몇 명의 유저가 해당 스테이지에 도달했는지 알아야 함
# # 몇 명이 지나갔는지 알아야 함
def solution(N, stages):

    answer = [[0,_+1] for _ in range(N)]

    u = len(stages)

    idx = 0
    for q in range(1,N+1):
        n = stages.count(q)
        answer[idx][0] = n / u
        u -= 1
        
        idx += 1

    return answer

print(solution(4,[4,4,4,4,4]))