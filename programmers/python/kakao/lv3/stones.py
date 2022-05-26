#https://programmers.co.kr/learn/courses/30/lessons/64062
from operator import indexOf

def solution(stones, k):
    limits = sorted(list(set(stones)))
    answer = int(len(limits)/2)
    while len(limits) > 2:
        can = [x for x in range(len(stones)) if stones[x] > answer]
        breakout = False
        for s in range(len(can)-1):
            if can[s+1] - can[s] > k:
                limits = [x for x in limits if x <= answer]
                breakout = True
                break
        if breakout == False:
            limits = sorted([ x for x in limits if x >= answer])
        answer = limits[int(len(limits)/2)]
    return limits[-1]
print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3))        