# 1,2,4로 만드는 숫자의 자리수와 시작 자연수
# otf_lst[1] == 3 == 1자리 자연수는 3까지
# otf_lst[2] == 12 == 2자리 자연수는 3부터 12까지
otf_lst = [0 for _ in range(19)]
for q in range(1,19):
    otf_lst[q] = otf_lst[q-1] + 3**q

    if otf_lst[q] > 500000000:
        break
otf = ['1','2','4']

def solution(n):

    # n의 자리수 찾기
    digit = 0
    for w in range(1,19):
        if otf_lst[w] >= n:
            digit = w
            break

    temp = ''

    # 시작위치
    s = otf_lst[digit-1]

    # 도착위치
    g = n
    for e in range(digit):

        if g != s:
            ee = (g-s) / (3**(digit-e-1))
            if ee <= 1:
                temp += otf[0]

            elif ee <= 2:
                temp += otf[1]

            else:
                temp += otf[2]

            s += (3**(digit-e-1)) * int(ee)

        else:
            temp += otf[(g-s)%3-1]

    answer = temp
    return answer

print(solution(30))