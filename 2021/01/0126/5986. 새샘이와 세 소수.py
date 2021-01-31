import sys
sys.stdin = open('5986. 새샘이와 세 소수.txt')

# 전체 수 범위
array = list(range(2,1000))

# array 앞에 0 2개 붙여줘서 범위 1000개로 맞춰주기(계산 귀찮아서...)
for plus in range(2):
    array.insert(0,0)

# 소수
my_array = []
for q in range(1000):

    # 0이 아니고
    if array[q] != 0:

        for w in range(q,1000):

            # array[q]로 나눠서 나머지가 0이 되는 수(소수가 아닌 수)
            if q != w and array[w]%array[q] == 0:

                # array[w]는 나중에 계산 피하기 위해서 0으로 만들고
                array[w] = 0

        # array[q]는 my_array에 저장
        my_array.append(array[q])


T = int(input())

# 결과 저장 위치
res = []

for tc in range(1,1+T):

    # 정수
    n = int(input())

    # tc에서 필요한 소수 저장 위치
    temp_array = []

    # -4한 이유는 세 가지 소수 더했을 때
    # 2+2+@처럼 나오는 것이 가장 큰 숫자를 이용할 수 있는 경우이기 때문
    # ex) 2+3+(@-1) == 2+2+@
    for i in my_array:
        if i <= n-4:
            temp_array.append(i)

    # 세 수를 더해서 n이 되는 경우의 수
    cnt = 0

    idx = len(temp_array)

    for z in range(idx):
        for x in range(z,idx):
            for c in range(x,idx):
                if my_array[z]+my_array[x]+my_array[c] == n:
                    cnt += 1

    res.append(cnt)

# 1000개를 print해야 해서 따로 출력
for a in range(T):
    print('#{} {}'.format(a+1,res[a]))