from itertools import permutations

n,m = map(int,input().split())

arr = [_ for _ in range(1,n+1)]

for q in permutations(arr,m):
    print(' '.join(map(str,q)))