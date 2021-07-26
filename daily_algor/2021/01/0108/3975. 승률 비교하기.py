import sys
sys.stdin = open('3975. 승률 비교하기.txt')

T = int(input())

for tc in range(1,1+T):
    a,b,c,d = map(int,input().split())

    ALICE = a/b
    BOB = c/d

    if ALICE > BOB:
        print('#{} {}'.format(tc,'ALICE'))
    elif BOB > ALICE:
        print('#{} {}'.format(tc,'BOB'))
    else:
        print('#{} {}'.format(tc,'DRAW'))

# 시간 초과

T = int(input())

res = []

for q in range(T):
    a,b,c,d = map(int,input().split())

    ALICE = a/b
    BOB = c/d

    if ALICE > BOB:
        res.append('ALICE')
    elif BOB > ALICE:
        res.append('BOB')
    else:
        res.append('DRAW')

for w in range(T):
    print('#{} {}'.format(w+1,res[w]))

# 통과
# 100000만개 print하는 출력이 시간을 오래 잡아먹는듯
# print는 생각보다 무겁다?