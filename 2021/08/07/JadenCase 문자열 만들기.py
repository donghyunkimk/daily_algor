def solution(s):
    answer = ''

    s = ' ' + s

    for q in range(1, len(s)):
        if s[q - 1] == ' ':
            answer += s[q].upper()

        else:
            answer += s[q].lower()

    return answer