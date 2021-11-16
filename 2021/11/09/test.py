n, k = map(int, input().split())
save = [_ for _ in range(1, n + 1)]

idx = 0
cur = len(save)
while True:
    if idx + k - 1 <= cur - 2:
        save.pop(idx)
        idx += (k - 1)

    else:
        save.pop(idx)
        idx = idx + k - cur
        while idx > cur - 1:
            idx -= (cur - 1)

    cur -= 1

    if cur == 2:
        break

print(save)


#
# 2 3 9 3
# 4 9 9 1
# 9 9 1 4
# 2 1 1 9