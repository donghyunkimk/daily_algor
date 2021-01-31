import sys
sys.stdin = open('4466. 최대 성적표 만들기.txt')

def search(num, idx, cnt):
    global max_score
    if cnt == k-1:
        if max_score - 100 > num:
            return

    if cnt == k:
        if max_score < num:
            max_score = num
            return


    for w in range(idx,n):
        search(num+my_score[w],w+1,cnt+1)

    return


T = int(input())

for tc in range(1,1+T):
    n,k = map(int,input().split())

    my_score = list(map(int,input().split()))

    max_score = 0

    for q in range(n):
        search(my_score[q],q+1,1) # 현재 점수, idx, cnt

    print('#{} {}'.format(tc,max_score))