n = int(input())

# n_length = len(str(n))
#
# ans = 0
# if n > 10:
#     for q in range(n-n_length*9,n):
#         if q > 0:
#             number = sum(map(int, str(q))) + q
#             if number == n:
#                 ans = q
#                 break
#
# print(ans)
ans = 0
for q in range(1,n+1):
    num = sum(map(int,str(q))) + q
    if num == n:
        ans = q
        break

print(ans)
