def solution(left, right):
    answer = 0

    for q in range(left,right+1):
        temp = []
        for w in range(1,int(q**(1/2)+1)):
            if q % w == 0:
                if w ** 2 == q:
                    temp.append(w)

                else:

                    temp.append(q//w)
                    temp.append(w)

        if len(temp) % 2 == 0:
            answer += q

        else:
            answer -= q

    return answer

print(solution(13,17))