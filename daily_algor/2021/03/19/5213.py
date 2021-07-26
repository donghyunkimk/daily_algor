T = int(input())

# 약수 중 홀수의 합을 저장할 배열
store = [0]*1000001
store[1] = 1
store[2] = 1

# store의 n번 인덱스까지의 합을 저장할 배열
store_sum = [0]*1000001
store_sum[1] = 1
store_sum[2] = 2

for q in range(3,1000001):
    temp = 0

    # 2의 배수의 약수 중 홀수의 합은 store[2]*store[q//2]
    if q%2 == 0:
        store[q] = store[q//2]
        store_sum[q] = store_sum[q-1]+store[q]

    else:

        # n의 약수를 찾기 위해 1부터 n까지 볼 필요 없음
        # 제곱근까지만 보면 됨
        # 위에서 2의 배수를 확인했기 때문에 여기서는 확인할 필요 없음
        for w in range(1,int(q**0.5)+1,2):

            # 약수 확인
            if q%w == 0:

                # 홀수 확인
                if w % 2 == 1:
                    temp += w

                # 제곱근인 경우 두번 더하는 것 방지하기 위해 w*w != q
                if w*w != q and q//w%2 == 1:
                    temp += q//w

        store[q] = temp
        store_sum[q] = store_sum[q-1]+store[q]


res = [0]*(T+1)

for tc in range(1,1+T):
    l,r = map(int,input().split())

    res[tc] = store_sum[r] - store_sum[l-1]

for e in range(1,1+T):
    print('#{} {}'.format(e,res[e]))