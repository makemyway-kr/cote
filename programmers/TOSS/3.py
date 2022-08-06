from itertools import permutations
from re import L
def solution(k,dungeons):
    answer = 0
    routes = permutations(dungeons,len(dungeons))
    for r in routes:
        curr = k
        visitied = 0
        for d in r:
            if curr < d[0]:
                break
            visitied += 1
            curr -= d[1]
        if visitied > answer:
            answer = visitied
        if answer == len(dungeons):
            break
    return answer