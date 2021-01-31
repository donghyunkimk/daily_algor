import sys
sys.stdin = open('7675. 통역사 성경이.txt')

T = int(input())

end_item = ['.', '!', '?']

for tc in range(1,1+T):

    # 문장의 개수
    n = int(input())

    # 문장
    sentence = list(map(str,input().split()))

    cnt = 0

    res = []

    for q in sentence:
        if len(q) == 1:
            if q[0].isupper():
                cnt += 1

        else:


            if q[-1] not in end_item:
                if q[0].isupper() and q[1:].isalpha() and q[1:].islower():
                    cnt += 1

            else:
                if q[0].isupper() and q[1:len(q)-1].isalpha() and q[1:len(q)-1].islower():
                    cnt += 1

                res.append(cnt)
                cnt = 0

    print('#{}'.format(tc),*res)