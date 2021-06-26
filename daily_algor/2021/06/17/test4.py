def floatToString():
    number_lst = []

    idx = 0
    while True:
        if n > 0:
            if n // (10 ** idx) == 0:
                break

        elif n < 0:
            if n // -(10 ** idx) == 0:
                break
        idx += 1

    i_idx = 0
    while True:
        if n > 0:
            if n // ((10**i_idx)**0.5) == 0:
                break

        elif n < 0:
            if n // -(10 ** i_idx) == 0:
                break
        i_idx += 1
        print(n//10**i_idx)

    print(i_idx)

    cnt = 0
    if n > 0:
        for q in range(idx - 1, -i_idx, -1):
            number_lst.append(int(n / (10 ** q) % 10))
            cnt += 1
            if cnt == idx:
                number_lst.append('.')

    elif n < 0:
        for q in range(idx - 1, -i_idx, -1):
            number_lst.append(int(n / -(10 ** q) % 10))
            cnt += 1
            if cnt == idx:
                number_lst.append('.')

    temp_res = ''.join(map(str,number_lst))

    return '-'+temp_res

n = -101.937

res = floatToString()

print(res)