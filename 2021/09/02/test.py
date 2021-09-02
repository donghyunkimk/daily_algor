def solution(phone_book):
    phone_book.sort()

    answer = True
    book_l = len(phone_book)
    book_idx = 0
    while True:
        book_w = phone_book[book_idx][0]
        temp = []
        for q in range(book_idx, book_l):
            if book_w == phone_book[q][0]:
                temp.append(phone_book[q])

            else:
                book_idx = q
                break

        idx = 0
        temp.sort()
        while True:
            word = temp[idx]
            word_l = len(word)
            for q in range(idx + 1, len(temp)):
                if word == temp[q][0:word_l]:
                    answer = False
                    break

            idx += 1

            if answer == False or idx == len(temp) - 1:
                break

        if answer == False or book_idx == len(phone_book) - 1:
            break

    return answer

print(solution(["123","456","789"]))