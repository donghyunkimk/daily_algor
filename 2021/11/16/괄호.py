n = int(input())

for q in range(n):
    check = 0
    board = list(str(input()))

    word = []
    for w in board:
        if w == '(':
            word.append('(')

        else:
            if len(word) == 0:
                check = 1
                break

            else:
                if word[-1] == '(':
                    word.pop(-1)

    if check == 1 or len(word) != 0:
        print('NO')
    else:
        print('YES')