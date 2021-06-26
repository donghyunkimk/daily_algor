left = ['E','S','T','J']
right = ['I','N','F','P']

# input 값
gil = str(input())

# 바꾼 단어 저장용
res = ''

for q in gil:

    # q가 left 안에 있으면
    if q in left:

        # right[left 안의 q 위치값]
        res += right[left.index(q)]
    else:
        res += left[right.index(q)]

print(res)