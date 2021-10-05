def solution(arr):
    answer = []

    temp = -1
    for q in range(1, len(arr) - 1):
        if arr[q - 1] == arr[q] and temp == -1:
            temp = arr[q]

        elif arr[q - 1] != arr[q]:
            answer.append(arr[q - 1])

            if temp != -1:
                temp = -1

    if arr[-2] == arr[-1]:
        answer.append(arr[-1])
    else:
        answer.append(arr[-2])
        answer.append(arr[-1])

    return answer