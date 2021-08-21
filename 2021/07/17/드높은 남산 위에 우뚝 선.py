n = int(input())

lst = list(map(int,input().split()))

cur_num = 0
check = 0

for q in lst:
    if check == 0:
        if q > cur_num:
            cur_num = q

        elif q == cur_num:
            check = 2
            break

        else:
            check = 1
            cur_num = q

    elif check == 1:
        if cur_num > q:
            cur_num = q

        else:
            check = 2
            break

if check != 2:
    print('YES')

else:
    print('NO')