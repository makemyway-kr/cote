#추석트래픽 문제
from selectors import EpollSelector


def solution(lines):
    answer = 0
    if len(lines) == 1:
        return 1
    sf = []
    for l in lines:
        temp = l.split(' ')
        duration = float(temp[2][0:-1])
        finTime = temp[1].split(':')
        finTimeinSec = float(int(finTime[0])*60*60 + 60*int(finTime[1])) + float(finTime[2])
        startTimeinSec = int(finTimeinSec * 1000) - int(duration * 1000) + 1
        sf.append([startTimeinSec, int(finTimeinSec*1000)])
    headTime = sf.sort(key = lambda x : x[1])[-1][1]
    tailTime = sf.sort(key = lambda x : x[0])[0][0]
    minTime = (tailTime + headTime) / 2
    sf.sort(key = lambda x : x[0])
    while tailTime - headTime > 1999:
        temp = [[],[],[]]
        for s in range(len(sf)):
            if sf[s][1] < minTime:
                temp[0].append(s)
            elif sf[s][1] == minTime or sf[s][0] == minTime :
                temp[1].append(s)
            elif sf[s][0] > minTime:
                temp[1].append(s)
        if len(temp[0]) + len(temp[1]) > len(temp[1]) + len(temp[2]):
            tailTime = minTime
            for t in temp[2]:
                sf.pop(t)
        elif len(temp[0]) + len(temp[1]) < len(temp[1]) + len(temp[2]):
            headTime = minTime
            for t in temp[0]:
                sf.pop(t)
        else:
            return len(temp[0]) + len(temp[1])
        minTime = (headTime + tailTime)/2
    max = 0
    for t in range(headTime,tailTime-999,0.001):
        count = 0
        for s in sf:
            if s[0] > 
    return answer