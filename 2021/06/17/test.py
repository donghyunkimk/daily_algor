def find():
    if n >= 0:
        for q in range(len(n_lst)):
            if int(n_lst[q]) < 7:
                n_lst.insert(q,'7')
                break
            if q == len(n_lst)-1:
                n_lst.insert(q+1,'7')
    else:
        for q in range(1,len(n_lst)):
            if int(n_lst[q]) > 7:
                n_lst.insert(q, '7')
                break
            if q == len(n_lst) - 1:
                n_lst.insert(q+1,'7')
    return
n = int(input())
n_lst = list(str(n))
find()
res = ''
for w in n_lst:
    res += w

print(int(res))
