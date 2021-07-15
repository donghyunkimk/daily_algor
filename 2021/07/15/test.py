lst = [0 for _ in range(101)]
lst[1] = 1
lst[2] = 1

for q in range(98):
    lst[q+3] = lst[q]+lst[q+1]

T = int(input())

for tc in range(1,1+T):

    print('#{} {}'.format(tc,lst[int(input())]))