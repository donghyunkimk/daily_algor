T = int(input())

for tc in range(1, 1 + T):

    # 문자를 리스트로 받는 s
    s = list(input())

    # 종료 확인용 end
    end = False

    # for문 돌면서 count 값이 2이면 pass
    # 그 외에는 end를 True로 바꾸고 for문 종료
    for q in s:
        if s.count(q) == 2:
            pass

        else:
            end = True
            break

    if end == True:
        print('#{} {}'.format(tc, 'No'))

    else:
        print('#{} {}'.format(tc, 'Yes'))