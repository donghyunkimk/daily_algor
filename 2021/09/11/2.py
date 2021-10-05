def solution(n, k):
    answer = 0

    num_lst = "0123456789"
    a = []
    while n != 0:
        a.append(num_lst[n % k])
        n //= k

    word = ''.join(a[::-1])
    l_word = len(word)

    temp = ''
    idx = 0
    for q in word:
        if q == '0' and len(temp) != 0:
            t_num = int(temp)
            check = 0
            if t_num == 1:
                check = 1

            for w in range(2,int(t_num**(1/2))+1):
                if t_num % w == 0:
                    check = 1
                    break

            if check == 0:
                answer += 1

            temp = ''

        elif idx == l_word - 1 and q != '0':
            temp += q
            t_num = int(temp)
            check = 0
            if t_num == 1:
                check = 1

            for w in range(2, int(t_num ** (1 / 2)) + 1):
                if t_num % w == 0:
                    check = 1
                    break

            if check == 0:
                answer += 1

        elif q != '0':
            temp += q

        idx += 1

    if l_word == 1 and int(word) == 1:
        answer = 0

    return answer

print(solution(11,10))

# 한문제 틀림