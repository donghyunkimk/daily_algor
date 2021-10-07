# 현재 위치, 뽑은 수, 현재까지 완성된 단어
def find(idx,cnt,word):

    # 알파벳을 다 뽑았으면
    if cnt == l:
        v_num = word.count('a') + word.count('e') + word.count('i') + word.count('o') + word.count('u')

        # 모음 1개 이상, 자음 2개 이상 조건 확인
        if l - v_num >= 2 and v_num >= 1:
            word.sort()
            answer.append(''.join(word))

    for q in range(idx,c):
        find(q+1,cnt+1,word+[board[q]])

    return

l,c = map(int,input().split())

board = list(map(str,input().split()))

answer = []

find(0,0,[])

answer.sort()

for w in answer:
    print(w)