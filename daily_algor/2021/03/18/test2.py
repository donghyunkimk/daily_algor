import timeit
start_time = timeit.default_timer()  # 시작 시간 체크
#
# T = int(input())

square = [0]*(10**7+1)
#
# idx = 2
#
# while True:
#     if square[idx] != 1:
#         for q in range(idx,10**7+1):
#             if square[q]%idx == 0:
#                 cnt = 0
#                 while True:
#                     if square[q]%idx == 0:
#                         cnt += 1
#                         square[q] = square[q]//idx
#
#                     else:
#                         break
#
#                 if cnt%idx == 1:
#                     square[q] *= idx
#
#     idx += 1
#     if idx >= 3500:
#         break

print(square)

terminate_time = timeit.default_timer()  # 종료 시간 체크

print("%f초 걸렸습니다." % (terminate_time - start_time))