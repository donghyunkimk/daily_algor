def solution(n, info):
    global max_score
    global score_lst

    max_score = 0
    score_lst = []

    for q in range(1,n+1):
        for w in range(11):
            if 11 - w < q:
                pass

            else:
                dfs(n,w,[w],info,q)

    if len(score_lst) == 0:
        answer = [-1]
    else:
        for z in range(len(score_lst)):
            score_lst[z] = list(reversed(score_lst[z]))

        score_lst.sort(reverse=True)

        answer = list(reversed(score_lst[0]))

    return answer

def dfs(l,idx,choice_arr,apeech_info,digit):
    global max_score
    global score_lst

    if digit == len(choice_arr):
        number = l
        cnt = digit
        apeech = 0
        lion = 0
        temp_info = [0 for _ in range(11)]
        for r in range(11):
            if r in choice_arr:
                if number > apeech_info[r]:
                    if cnt == 1:
                        temp_info[r] = number
                        number = 0

                    else:
                        temp_info[r] = apeech_info[r] + 1
                        number -= temp_info[r]

                    lion += 10 - r

                else:
                    if cnt == 1:
                        temp_info[r] = number
                        number = 0

                    apeech += 10 - r

                cnt -= 1

            else:
                if apeech_info[r] != 0:
                    apeech += 10-r

        if lion > apeech:
            if lion - apeech > max_score:
                max_score = lion - apeech
                score_lst = [temp_info]

            elif lion - apeech == max_score:
                score_lst.append(temp_info)

        return

    for e in range(idx+1,11):
        dfs(l,e,choice_arr+[e],apeech_info,digit)

    return

print(solution(10,[0,0,0,0,0,0,0,0,3,4,3]))

# 어피치가 n발 다 쏜 후 라이언 n발 쏘기
# 점수 계산
# k 점을 더 많이 맞힌 사람이 k점 획득(동률일 경우 어피치가 가져감)
# 어느 누구도 못 맞춘 경우 안 가져감
# 최종 점수가 높을 경우 어피치 우승
# 어피치는 다 쐈고, 라이언 쏠 차례
# 가장 큰 점수차이로 이기기 위해 어느 과녁에 맞혀야 하는지 구하기
# n 화살의 개수 info 어피치가 맞힌 과녁 점수의 개수 10 ~ 0 순서대로
