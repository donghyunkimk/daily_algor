T = int(input())

# 핸드폰 키패드
keyboard = [0,
            0,
            ['a','b','c'],
            ['d','e','f'],
            ['g','h','i'],
            ['j','k','l'],
            ['m','n','o'],
            ['p','q','r','s'],
            ['t','u','v'],
            ['w','x','y','z']]

for tc in range(1,1+T):

    # 키 입력, 단어의 개수
    s, n = map(int,input().split())

    # 단어
    word = list(map(str,input().split()))

    # 키 입력에 대응되는 사전 안의 단어 수
    cnt = 0

    # 키 입력(int) => 리스트 형태
    s_lst = list(str(s))

    # 키 입력의 길이
    s_len = len(s_lst)

    for q in range(n):

        # 키 입력에 맞는 단어가 몇 개인가
        temp = 0

        if len(word[q]) == s_len:
            for w in range(s_len):
                if word[q][w] in keyboard[int(s_lst[w])]:
                    temp += 1

                else:
                    break

        if temp == s_len:
            cnt += 1

    print('#{} {}'.format(tc,cnt))