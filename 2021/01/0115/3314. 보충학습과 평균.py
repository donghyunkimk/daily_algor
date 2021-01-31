import sys
sys.stdin = open('3314. 보충학습과 평균.txt')

import timeit

start_time = timeit.default_timer()

T = int(input())

# scores = []

for tc in range(1,1+T):
    score = list(map(int,input().split()))

    res = 0

    for q in score:
        if q >= 40:
            res += q
        else:
            res += 40

    print('#{} {}'.format(tc,res//5))

terminate_time = timeit.default_timer()

print("%f초 걸렸습니다." % (terminate_time - start_time))
#
#     scores.append(res//5)
#
# for w in range(T):
#     print('#{} {}'.format(w+1,scores[w]))