# 계산해야하는 숫자의 위치, 현재까지 결과값, 사칙연산 사용 확인
def dfs(idx, temp, check):
    global max_car
    global min_car

    # 탈출조건
    if n == idx:
        if max_car < temp:
            max_car = temp

        if min_car > temp:
            min_car = temp

        return

    for w in range(4):

        # 주어진 사칙연산 개수(?)와 현재까지 사용한 사칙연산 비교
        if check[w] < items[w]:
            if item_detail[w] == '+':
                check[w] += 1
                dfs(idx + 1, temp + numbers[idx], check)

                # 이전 상태로 돌리기 위해
                check[w] -= 1

            elif item_detail[w] == '-':
                check[w] += 1
                dfs(idx + 1, temp - numbers[idx], check)
                check[w] -= 1

            elif item_detail[w] == '*':
                check[w] += 1
                dfs(idx + 1, temp * numbers[idx], check)
                check[w] -= 1

            else:
                check[w] += 1

                # temp가 음수인 경우
                # numbers에 있는 숫자의 범위는 1 ~ 100이므로 고려 X
                if temp < 0:
                    dfs(idx + 1, -(abs(temp) // numbers[idx]), check)

                # 양수인 경우
                else:
                    dfs(idx + 1, temp // numbers[idx], check)
                check[w] -= 1

    return

n = int(input())

# 계산해야 할 숫자들
numbers = list(map(int,input().split()))

# 사칙연산의 개수
items = list(map(int,input().split()))

# 최대값과 최소값
max_car = -1000000000
min_car = 1000000000

item_detail = ['+','-','*','/']

for q in range(4):
    # 사칙연산이 존재하면
    if items[q] != 0:
        if item_detail[q] == '+':
            dfs(2,numbers[0]+numbers[1],[1,0,0,0])

        elif item_detail[q] == '-':
            dfs(2,numbers[0]-numbers[1],[0,1,0,0])

        elif item_detail[q] == '*':
            dfs(2,numbers[0]*numbers[1],[0,0,1,0])

        else:
            dfs(2,numbers[0]//numbers[1],[0,0,0,1])

print(max_car)
print(min_car)