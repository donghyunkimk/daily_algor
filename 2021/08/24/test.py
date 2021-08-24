def solution(record):
    user = dict()
    cnt = 0
    for q in range(len(record)):

        # split을 통해 E + n + t + e + r로 이루어진 단어를 'Enter'로 만들기
        record[q] = record[q].split()

        # Leave가 아니면 user값 갱신
        if record[q][0] != 'Leave':
            user[record[q][1]] = record[q][2]

        if record[q][0] != 'Change':
            cnt += 1

    answer = [0 for _ in range(cnt)]
    idx = 0
    for e in record:
        if e[0] == 'Enter':
            answer[idx] = user[e[1]] + '님이 들어왔습니다.'
            idx += 1

        elif e[0] == 'Leave':
            answer[idx] = user[e[1]] + '님이 나갔습니다.'
            idx += 1

    return answer