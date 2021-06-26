for tc in range(10):
    n = int(input())

    word = [list(input()) for _ in range(100)]

    max_len = 1

    for q in range(100):
        for w in range(100):
            # 가로
            for e in range(w,100):

            # 세로