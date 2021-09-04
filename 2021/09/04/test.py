def solution(priorities, location):
    answer = 0

    # 탈출 조건
    check = 0
    while True:
        # 출력할 숫자
        n = priorities[0]

        for q in range(len(priorities)):

            # 현재 위치의 값이 출력할 숫자보다 크면
            # 출력할 숫자를 priorities의 끝으로 보내기
            # location값(내가 확인하고 싶은 값의 index) 갱신
            if priorities[q] > n:
                priorities.append(priorities.pop(0))
                if location == 0:
                    location = len(priorities) - 1

                else:
                    location -= 1
                break

            # for문 다 돌았는데도 출력할 숫자보다 큰 값을 못 찾은 경우
            # 출력할 값 제외
            # location 값이 0인 경우 == 이번에 출력해야 할 경우
            else:
                if q == len(priorities) - 1:
                    answer += 1
                    priorities.pop(0)
                    if location == 0:
                        check = 1

                    else:
                        location -= 1

        if check == 1:
            break

    return answer