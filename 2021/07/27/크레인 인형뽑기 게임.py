def solution(board, moves):
    answer = 0

    n = len(board)

    moves_n = len(moves)

    # 뽑는 값들 저장
    bucket = [-1 for _ in range(moves_n)]

    # board 방문 확인
    check = [[0 for _ in range(n)] for q in range(n)]

    # bucket의 위치
    # 중간에 -1 끼는거 방지하기 위함
    bucket_idx = 0
    for w in moves:
        for e in range(n):

            # 0이 아니고, 방문한적 없으면 뽑기
            if board[e][w - 1] != 0 and check[e][w - 1] == 0:
                check[e][w - 1] = 1
                bucket[bucket_idx] = board[e][w - 1]
                bucket_idx += 1
                break

    while True:

        # 탈출 조건
        temp = bucket[:]

        # bucket[r]의 값과 bucket[r+1]의 값이 같으면
        # -1끼리 터지는거 방지하기 위한 -1 조건
        for r in range(len(bucket) - 1):
            if bucket[r] == bucket[r + 1] and bucket[r] != -1:
                answer += 2
                del bucket[r:r+2]
                break

        if bucket == temp:
            break

    return answer