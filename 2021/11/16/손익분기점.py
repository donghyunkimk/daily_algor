# A 고정 B 가변 C 가격
# 최초 이익 발생 시점

a,b,c = map(int,input().split())

if b >= c:
    print(-1)

else:
    print(a//(c-b) + 1)