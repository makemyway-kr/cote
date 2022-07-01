# lv2 전화번호 목록
def solution(phone_book):
    answer = True
    hashed = {}
    phone_book.sort(key=lambda x: len(x))
    key_length = len(phone_book[0])
    for p in phone_book:
        if p[0:key_length] in hashed.keys():
            for k in hashed[p[0:key_length]]:
                if k == p[0:len(k)]:
                    answer = False
                    break
            hashed[p[0:key_length]].append(p)
        else:
            hashed[p[0:key_length]] = [p]
        if answer == False:
            break
    return answer
