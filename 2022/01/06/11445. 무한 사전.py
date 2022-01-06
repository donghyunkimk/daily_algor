t = int(input())

for tc in range(1,1+t):
    p = str(input()).rstrip()
    q = str(input()).rstrip()

    word = p + 'a'
    if word == q:
        print('#{} {}'.format(tc,'N'))
    else:
        print('#{} {}'.format(tc,'Y'))