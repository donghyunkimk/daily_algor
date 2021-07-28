def solution(new_id):
    answer = ''

    # 대문자 -> 소문자
    temp = new_id[:].lower()

    # 소문자, 숫자, -, _, . 제외한 모든 문자 제거
    temp_answer = ''
    for q in temp:
        if (97 <= ord(q) <= 122) or (48 <= ord(q) <= 57) or (45 <= ord(q) <= 46) or ord(q) == 95:
            temp_answer += q

    # ... 치환
    check = 0
    for w in temp_answer:
        if check == 0:
            if w == '.':
                check = 1

            else:
                answer += w

        else:
            if w != '.':
                check = 0
                answer += '.' + w

    # . 처음 끝 제거
    answer = answer.strip('.')

    # 빈 문자열일 경우 a입력
    if len(answer) == 0:
        answer = 'a'

    # 16자리 이상 :16까지만 출력, 마지막이 . 이면 . 제거
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer.rstrip('.')

    # 2자 이하면, 마지막 문자 3이 될 때까지 반복
    if len(answer) <= 2:
        while True:
            answer += answer[-1]
            if len(answer) == 3:
                break

    return answer