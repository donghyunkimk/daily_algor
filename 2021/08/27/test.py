m = [2,2]
b = [3,2,1,2]

easy = [0,1,2,4,8,16,32]

idx = 0
for q in m:
    temp = b[idx:idx+m]
    cnt = 0
    for w in temp:
