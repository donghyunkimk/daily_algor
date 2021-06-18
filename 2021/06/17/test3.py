n = -10.909
m = -10.97

number_lst = []

idx = 0
while True:
    if n > 0:
        if n//(10**idx) == 0:
            break

    elif n < 0:
        if n//-(10**idx) == 0:
            break
    idx += 1

print(idx)

cnt = 0
for q in range(idx-1,-4,-1):
    number_lst.append(int(n/(10**q)%10))
    cnt += 1
    if cnt == idx:
        number_lst.append('.')

for w in range(idx-1,-4,-1):
    number_lst.append(int(n / -(10 ** w) % 10))
    cnt += 1
    if cnt == idx:
        number_lst.append('.')

number_lst.reverse()
# for w in range(len(number_lst)):
#     if number_lst[w] == 0:


# res = ''
# for w in

print(number_lst)
