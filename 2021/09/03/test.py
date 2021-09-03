# dict형태를 2개 만들어서 'A' : 1, 1 : 'A' 형태로 만들어 두기
# 글자 바꿀 때 사용
alpha = dict()

i = 65
for q in range(1,27):
    alpha[chr(i)] = q
    i += 1

r_alpha = dict()

i = 65
for q in range(1,27):
    r_alpha[q] = chr(i)
    i += 1

def solution(name):
    n = len(name)

    # 글자, idx, cnt
    temp = [['A'*n,0,0]]

    while True:
        word, idx, cnt = temp.pop(0)

        if name[idx] != word[idx]:

            word = word[:idx] + name[idx] + word[idx+1:]

            # 알파벳 이동 순서 결정
            if 26 - alpha[word[idx]] + 1 > alpha[word[idx]] - 1:
                cnt += alpha[word[idx]] - 1

            else:
                cnt += 26 - alpha[word[idx]] + 1

        # 탈출조건
        # 현재까지 이동한 값이 목표 값(name)과 같은지 확인
        if word != name:

            # 오른쪽 이동
            temp.append([word,(idx+1)%n,cnt+1])

            # 왼쪽 이동
            # 왼쪽 이동의 경우 0 - 1의 경우 존재하기 때문에 2가지 경우로 나눠서 확인
            if idx == 0:
                temp.append([word,n-1,cnt+1])
            else:
                temp.append([word,idx-1,cnt+1])
        else:
            break

    answer = cnt
    return answer