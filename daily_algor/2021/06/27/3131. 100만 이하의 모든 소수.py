num = [_ for _ in range(3,10**6,2)]
check = [0 for _ in range(3,10**6,2)]

n = len(num)

res = [2]

idx = 0

while True:
    idx_check = 0
    temp_num = num[idx]
    res.append(temp_num)
    for q in range(idx+1,n):
        if check[q] == 0:
            if num[q] % temp_num == 0:
                check[q] = 1

            else:
                if idx_check == 0:
                    idx = q
                    idx_check = 1