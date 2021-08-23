# 모든 경우의 테이블은 동일
table_lst = [["SI", "JAVA", "JAVASCRIPT", "SQL", "PYTHON", "C#"],
             ["CONTENTS", "JAVASCRIPT", "JAVA", "PYTHON", "SQL", "C++"],
             ["HARDWARE", "C", "C++", "PYTHON", "JAVA", "JAVASCRIPT"],
             ["PORTAL", "JAVA", "JAVASCRIPT", "PYTHON", "KOTLIN", "PHP"],
             ["GAME", "C++", "C#", "JAVASCRIPT", "C", "JAVA"]]


def solution(table, languages, preference):
    answer = ''
    max_num = 0
    max_lan = []

    for e in range(5):
        temp_score = 0
        for r in range(len(languages)):
            if languages[r] in table_lst[e]:
                temp_score += preference[r] * (6 - table_lst[e].index(languages[r]))

        if temp_score > max_num:
            max_num = temp_score
            max_lan = [table_lst[e][0]]

        elif temp_score == max_num:
            max_lan.append(table_lst[e][0])

    max_lan.sort()
    answer = max_lan[0]

    return answer