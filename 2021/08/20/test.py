def solution(s):
    answer = []

    answer_lst = []
    temp_lst = []
    for q in range(1, len(s) - 1):

        # {에서 시작
        if s[q] == '{':
            temp = ''

        # }에서 초기화 및 answer_lst에 현재까지의 값들 추가
        elif s[q] == '}':
            temp_lst.append(int(temp))
            temp = ''
            answer_lst.append(temp_lst)
            temp_lst = []

        # ,는 두 가지 경우 있음
        # 숫자,숫자 의 경우와 },{의 경우
        # },{의 경우에 또 추가하지 않기 위해서 len 조건 추가
        elif s[q] == ',':
            if len(temp) != 0:
                temp_lst.append(int(temp))
                temp = ''

        # 그 외는 숫자라 그냥 추가
        else:
            temp += s[q]

    # 원소의 길이에 따른 정렬
    answer_lst.sort(key=lambda x: len(x))

    for w in answer_lst:
        for e in w:
            if e not in answer:
                answer.append(e)

    return answer