def convert():

    temp_res = [0 for _ in range(word.count(' ')*2+1)]

    idx = 0
    temp = ''
    for q in word:

        if q != ' ':
            temp += q
            if q == word[-1]:
                temp_res[idx] = temp

        else:
            temp_res[idx] = temp
            temp_res[idx+1] = ' '
            temp = ''
            idx += 2

    temp_res.reverse()
    return temp_res

word = 'SSAFY JOB FAIR'

res = convert()

for w in res:
    print(w,end='')