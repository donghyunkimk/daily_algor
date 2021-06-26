import sys
sys.stdin = open('2005. 파스칼의 삼각형.txt')

def num_sum(num):
    temp = [0]*num # 숫자 더해줄 0 리스트 만들기

    for qq in range(num-1):
        temp[-1-qq] += numbers[-1-qq]
        temp[-2-qq] += numbers[-1-qq]

    numbers.extend(temp) # 다 돌면 numbers에 temp 더 하기

T = int(input())

for tc in range(1,1+T):
    n = int(input())

    if n != 1:
        numbers = [1] # 처음 시작은 1이라 그냥 넣어 줌

        for q in range(2,n+1):
            num_sum(q)

        cnt = 0
        print('#{}'.format(tc))
        for w in range(n):
            for ww in range(w+1):
                print(numbers[cnt], end=' ')
                cnt += 1
            print()

    else:
        print('#{}'.format(tc))
        print(1)