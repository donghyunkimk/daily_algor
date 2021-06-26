import sys
sys.stdin = open('보물.txt')

# 정수의 길이
N = int(input())

# A 배열
A = list(map(int,input().split()))

# B 배열
B = list(map(int,input().split()))

# 정렬
A.sort()
B.sort(reverse=True)

# 결과
res = 0

for q in range(N):
    res += A[q] * B[q]

print(res)

N = int(input())

A = list(map(int,input().split()))

B = list(map(int,input().split()))

res = 0

# 최소 최대값 찾은 후 해당 값 제거
# 다음에 같은 값 찾지 않기 위함
for q in range(N):
    res += min(A) * max(B)

    A.remove(min(A))
    B.remove(max(B))

print(res)