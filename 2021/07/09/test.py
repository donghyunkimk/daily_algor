
participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
answer = ''
temp = 0
dic = {}
for part in participant:
    dic[hash(part)] = part
    temp += int(hash(part))

for com in completion:
    temp -= hash(com)

answer = dic[temp]

print(answer)

def solution(participant, completion):
    answer = ''

    participant.sort()
    completion.sort()

    for q in range(len(completion)):
        if participant[q] != completion[q]:
            answer = participant[q]
            break

        if q == len(completion) - 1:
            answer = participant[-1]

    #     temp = 0
    #     dic = {}
    #     for q in participant:
    #         dic[hash(q)] = q
    #         temp += hash(q)

    #     for w in completion:
    #         temp -= hash(w)

    #     answer = dic[temp]

    return answer