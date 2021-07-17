T = int(input())

for tc in range(1,1+T):

    word = list(input())

    cnt = 0

    alpha_check = [0 for _ in range(21)]

    for q in word:
        alpha_check[ord(q)-97] += 1

    odd = []

    for w in range(21):
        if alpha_check[w] != 0:
            if alpha_check[w] % 2 == 0:


            else:
                odd.append(w)

    print(odd)