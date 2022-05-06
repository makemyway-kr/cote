#https://programmers.co.kr/learn/courses/30/lessons/64064
from itertools import combinations, product
def solution(user_id, banned_id):
    answer = []
    idLength = {}
    candidates = []
    for i in user_id:
        if len(i) not in idLength.keys():
            idLength[len(i)] = [i]
        else:
            idLength[len(i)].append(i)
    for b in banned_id:
        temp = []
        for c in idLength[len(b)]:
            breaker = False
            for i in range(len(b)):
                if (b[i] != c[i]) and (b[i] != '*'):
                    breaker = True
                    break
            if breaker == False:
                temp.append(c)
        candidates.append(temp)
    combi = list((product(*candidates)))
    comparing = len(banned_id)
    for c in combi:
        if len(set(c)) == comparing and set(c) not in answer:
            answer.append(set(c))
    return len(answer)