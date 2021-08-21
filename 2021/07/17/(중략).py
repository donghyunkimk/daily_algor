n = int(input())

s = input()

if n <= 25:
    print(s)

elif n > 25:
    temp = s[11:-11]
    if '.' not in temp or (temp.count('.') == 1 and temp[-1] == '.'):
        res = s[:11] + '...' + s[-11:]

    else:
        res = s[:9] + '......' + s[-10:]

    print(res)