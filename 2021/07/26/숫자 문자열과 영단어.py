numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

num_dic = {}

for q in range(10):
    num_dic[numbers[q]] = q

def solution(s):
    answer = ''

    idx = 0

    while True:

        # 숫자일 경우
        if 48 <= ord(s[idx]) <= 57:
            answer += str(s[idx])
            idx += 1

        # 영어 단어일 경우
        else:
            temp = ''
            while True:

                # key 값이 없으면
                if num_dic.get(temp) == None:
                    temp += s[idx]
                    idx += 1

                # key 값이 존재하면
                else:
                    answer += str(num_dic.get(temp))
                    break

        if idx == len(s):
            break

    answer = int(answer)

    return answer