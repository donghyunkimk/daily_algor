# 이번에 뽑을 모음의 수, 현재 위치, 현재까지의 단어, 현재까지 뽑은 모음의 수
def v_find(v_goal,v_idx,v_word,v_cnt):

    # 모음을 다 뽑았으면
    # 자음 뽑으러
    if v_goal == v_cnt:
        e_find(0,v_word,v_cnt)

        return

    for e in range(v_idx,v):
        v_find(v_goal,e+1,v_word+[v_alpha[e]],v_cnt+1)

    return

# 현재 위치, 현재까지 완성된 단어, 현재까지 뽑은 알파벳의 누적 수
def e_find(e_idx,e_word,e_cnt):

    # l과 현재까지 뽑은 알파벳 수가 같은 경우
    if l == e_cnt:
        e_word.sort()
        answer.append(''.join(e_word))

        return

    for r in range(e_idx,c-v):
        e_find(r+1,e_word + [e_alpha[r]], e_cnt + 1)

    return

l,c = map(int,input().split())

board = list(map(str,input().split()))

# 결과 저장할 곳
answer = []

# 모음의 수
v = 0
# 모음 저장
v_alpha = []
# 자음 저장
e_alpha = []

for q in board:
    if q in ['a','e','i','o','u']:
        v_alpha.append(q)
        v += 1

    else:
        e_alpha.append(q)

# w = 이번에 뽑을 모음의 수
for w in range(1,min(l-1, v+1)):
    v_find(w,0,[],0)

answer.sort()

for e in answer:
    print(e)