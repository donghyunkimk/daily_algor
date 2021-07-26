T = int(input())

for tc in range(1,1+T):

    # 울음소리
    arr = list(str(input()))

    # 모든 문자 사용했는지 확인을 위한 배열
    visited = [0 for _ in range(len(arr))]

    # 개구리 최소 숫자
    res = -1

    # 한 번의 울음 안에 c가 몇 번 있는가(겹치게 우는 것이 몇 마리인가)
    cnt = 0

    # 시작 위치(c 부터 시작)
    idx = 0

    while True:

        # 임시 cnt(몇 마리인지), 초기화
        temp = 0

        # 임시 idx, 초기화
        temp_idx = 0

        # 울음소리 저장, 초기화
        word = ''

        # 시작 값이 c가 아니면 불가능함
        if arr[idx] != 'c':
            break

        else:
            for q in range(idx, len(arr)):
                if arr[q] == 'c':

                    # word가 '' 이면
                    # c로 만들고, 방문처리
                    if len(word) == 0:
                        word += arr[q]
                        visited[q] = 1

                    # word가 ''이 아니면
                    # temp_idx에 저장된 값이 없으면 q 저장
                    else:
                        if temp_idx == 0:
                            temp_idx = q

                    # 몇 마리인지 세기
                    temp += 1

                # word가 c인 경우
                elif arr[q] == 'r' and len(word) == 1 and visited[q] == 0:
                    word += arr[q]
                    visited[q] = 1

                # word가 cr인 경우
                elif arr[q] == 'o' and len(word) == 2 and visited[q] == 0:
                    word += arr[q]
                    visited[q] = 1

                # word가 cro인 경우
                elif arr[q] == 'a' and len(word) == 3 and visited[q] == 0:
                    word += arr[q]
                    visited[q] = 1

                # word가 croa인 경우
                elif arr[q] == 'k' and len(word) == 4 and visited[q] == 0:
                    word += arr[q]
                    visited[q] = 1

                    # 만일 arr[0:5]의 값이 croak인 경우
                    # temp_idx 값이 변하지 않아서 계속 0번에서 시작함
                    # 그런 경우를 방지하기 위해 temp_idx 값에 q+1 저장
                    if temp_idx == 0:
                        temp_idx = q+1
                    break

        # 배열을 끝까지 다 돌았을 때,
        if q == len(arr) - 1:

            # word가 croak를 완성하지 못하면
            if word != 'croak':
                break

            # visited의 값이 모두 1일 때
            # res에 cnt값 저장
            if visited.count(1) == len(arr):
                res = cnt
                break

            # 아닌 경우 그냥 종료
            else:
                break

        # 배열을 끝까지 돌지 않았을 경우
        else:

            # temp가 cnt값보다 크면 cnt에 temp값 저장
            if temp > cnt:
                cnt = temp

            # idx에 temp_idx값 저장
            idx = temp_idx

    print('#{} {}'.format(tc,res))