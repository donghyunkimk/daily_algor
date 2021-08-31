def solution(skill, skill_trees):

    answer = len(skill_trees)

    # 선행 스킬로만 이루어진 문자열 생성
    for q in skill_trees:
        temp = ''
        for w in q:
            if w in skill:
                temp += w

        # 글자를 비교해서 다른 것이 나오면 중단
        # 다른 것이 나온다 = 선행 스킬을 정상적으로 배우지 않음
        for e in range(len(temp)):
            if skill[e] != temp[e]:
                answer -= 1
                break

    return answer