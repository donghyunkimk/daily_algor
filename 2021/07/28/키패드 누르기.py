def solution(numbers, hand):
    answer = ''

    # 왼손과 오른손의 초기 위치 값
    left = [3, 0]
    right = [3, 2]

    for q in numbers:
        if q == 1 or q == 4 or q == 7:
            answer += 'L'
            left = [q // 3, 0]

        elif q == 3 or q == 6 or q == 9:
            answer += 'R'
            right = [q // 4, 2]

        else:
            if q == 2 or q == 5 or q == 8:
                x = q // 3

            else:
                x = 3

            # 목표 번호와 왼손, 오른손 과의 거리
            left_distance = abs(left[0] - x) + abs(left[1] - 1)
            right_distance = abs(right[0] - x) + abs(right[1] - 1)

            if left_distance > right_distance:
                answer += 'R'
                right = [x, 1]

            elif left_distance < right_distance:
                answer += 'L'
                left = [x, 1]

            # 거리가 같은 경우 주로 사용하는 손에 따라 결정
            else:
                if hand == 'left':
                    answer += 'L'
                    left = [x, 1]

                else:
                    answer += 'R'
                    right = [x, 1]

    return answer