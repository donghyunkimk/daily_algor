n = int(input())

numbers = list(map(int,input().split()))

# + - * //
items = list(map(int,input().split()))

max_car = 0
min_car = 1000000000

item_lst = []

four = ['+','-','*','/']

for q_idx in range(4):
    for w_idx in range(items[q_idx]):
        item_lst.append(four[q_idx])

for q in range(n-1):

    if q == 0 or item_lst[q] != item_lst[q-1]:
        if item_lst[q] == '+':
            del item_lst[q]
            temp_num = numbers[0] + numbers[1]
            dfs(2,temp_num)
            item_lst.insert(q, '+')

        elif item_lst[q] == '-':
            numbers[0] - numbers[1]

        elif item_lst[q] == '*':
            numbers[0] * numbers[1]

        else:
            numbers[0] // numbers[1]

    #
    # else:
    #     if item_lst[q] != item_lst[q-1]:
    #         if item_lst[q] == '+':
    #             pass
    #
    #         elif item_lst[q] == '-':
    #             pass
    #
    #         elif item_lst[q] == '*':
    #             pass
    #
    #         else:
    #             pass
    #
