import sys
sys.stdin = open('5356. 의석이의 세로로 말해요.txt')

T = int(input())

for tc in range(1,1+T):
    words = [list(map(str,input())) for _ in range(5)]

    # 문자열의 최대 길이 구하기
    # for문의 범위 정하기 위해
    max_len = 0

    # 매번 길이를 확인할 수 없기 때문에 length에 문자열의 길이를 저장
    length = []

    for word in words:
        length.append(len(word))
        if len(word) > max_len:
            max_len = len(word)


    res = ''
    for q in range(max_len):
        for w in range(5):
            if length[w] > q:
                res += words[w][q]

    print('#{} {}'.format(tc,res))