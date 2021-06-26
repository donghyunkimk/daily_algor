for tc in range(10):

    # tc의 길이
    n = int(input())

    # 계산식
    board = list(map(str,input()))

    # 연산자 + * 저장
    cal = []

    # 숫자 저장
    num = []

    for q in board:
        if q == '+' or q == '*':
            cal.append(q)

        else:
            num.append(int(q))

    # 결과
    res = 0

    # '*' 연산으로 나온 값을 저장
    temp = 1

    for w in range(int(n/2)):
        if w != int(n/2)-1:

            # 3 + a + b의 경우
            # 앞의 3이 a에 영향을 미치지 않으므로 res에 a를 더하면 됨
            # 그러나 3 * a + b의 경우
            # a가 앞의 3과의 연산에서 영향을 받으므로 temp에 a를 곱하고
            # 그 값을 res에 더하면 됨(그 후 temp 초기화)
            if cal[w] == '+':
                if temp != 1:
                    temp *= num[w]

                    res += temp
                    temp = 1

                else:
                    res += num[w]

            # 연산자가 '*'인 경우 바로 res에 값을 추가하지 않고 temp에 저장
            # 이는 * 연산이 언제 끝나는지에 대한 정보가 없기 때문
            else:
                temp *= num[w]

        # w == int(n/2)-1 인 경우
        # num[w+1] 뒤에 연산자가 존재하지 않음
        # 따라서 cal[w] 연산자에 따라 num[w+1]을 따로 처리해줘야 함
        else:
            if cal[w] == '+':
                if temp != 1:
                    temp *= num[w]

                    res += temp


                else:
                    res += num[w]

                res += num[w + 1]

            else:
                temp *= num[w] * num[w+1]

                res += temp

    print('#{} {}'.format(tc+1,res))