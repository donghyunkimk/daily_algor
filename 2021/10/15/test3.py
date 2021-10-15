n = int(input())

answer = 0

temp = n
while True:
    if temp < 10:
        temp = temp * 11
        answer += 1

    else:
        # 10의 자리, 1의 자리
        a = temp//10
        b = temp%10
        c = a + b
        d = c%10
        e = b*10+d
        temp = e
        answer += 1

    if temp == n:
        break

print(answer)