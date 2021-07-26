T = int(input())

square = [0]*3200

square_store = [0]*(10**7)

num = 10**7

while True:
    for q in range(10**4):
        temp = (q+1)**2
        if temp <= num:
            square[q] = temp

        else:
            break

    for qq in range(1,10**4):

    break


res = []

for tc in range(1,1+T):
    a = int(input())

    for w in square:
        if w%a == 0:
            res.append(w//a)
            break

idx = 1
for e in res:
    print('#{} {}'.format(idx,e))
    idx += 1