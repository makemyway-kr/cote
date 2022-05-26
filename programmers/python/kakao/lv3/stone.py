#https://programmers.co.kr/learn/courses/30/lessons/64062
def solution(stones, k):
    answer = 0
    diminish = [[x for x in range(len(stones))],[x for x in stones]]
    while True:
        out = False
        elList = []
        to_eliminate = min(diminish[1])
        for x in range(len(diminish[1])):
            if diminish[1][x] == to_eliminate:
                elList.append(diminish[0][x])
        diminish = [[x for x in diminish[0] if x not in elList] , [x for x in diminish[1] if x!= to_eliminate ]]
        for x in range(len(diminish[0])-1):
            if diminish[0][x+1] - diminish[0][x] > 3:
                out = True
                break
        if out == True:
            answer = to_eliminate
            break
        answer = to_eliminate
    return answer