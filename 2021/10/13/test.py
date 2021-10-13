# dict 형태로 만들어서 미리 10000까지의 합 저장
t = dict()
t[0] = 0
temp = 0
for q in range(1,10001):
    temp += q
    t[q] = temp

# 정답 저장
# tc가 100000개이므로 따로 출력하는 것이 속도가 빠름
answer = []

T = int(input())

for tc in range(1,T+1):
    a,b = map(int,input().split())

    # 두 막대 간의 차이
    c = b - a

    # K값 찾기
    res = t[c-1] - a

    answer.append(res)

for w in range(len(answer)):
    print('#{} {}'.format(w+1,answer[w]))