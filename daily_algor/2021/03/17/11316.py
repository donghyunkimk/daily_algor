# s,p,q,m = 5,7,2,11
#
# temp = [s]
#
# for i in range(20):
#     temp_sum = (p*temp[-1]+q)%m
#     temp.append(temp_sum)
#
# print(temp)

T = int(input())

for tc in range(1,1+T):
    s,p,q,m = map(int,input().split())

    check = [0]*m

    temp = s

    for i in range(2):
        temp_sum = (p*temp+q)%m
        temp = temp_sum

    check[temp] = 1
    cnt = 1

    for x in range(m):
        print(temp)
        print(temp_sum)
        temp_sum = (p * temp + q) % m
        print(temp_sum)
        temp = temp_sum
        print(temp)
        if check[temp] == 0:
            check[temp] = 1
            cnt += 1

        else:
            break

    print(cnt)