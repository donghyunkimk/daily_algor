T = int(input())

for tc in range(1,1+T):
    word = input()
    n = len(word)

    answer = n

    idx = 0
    while idx != n:
        temp = []
        for q in range(idx,n):
            temp.append(word[q])
            if temp == reversed(temp):
                answer += 1

        idx += 1

    print(answer)