from multiprocessing import Process
from operator import indexOf
#먼저 p들 다 찾고 그 중에 거리 2 이하인 애들 대상으로만 검사
#https://programmers.co.kr/learn/courses/30/lessons/81302
def search_and_catch(place):
    plist = []
    Xlist = []
    err = False
    for r in range(5):
        for c in range(5):
            if place[r][c] == 'P':
                plist.append([r,c])
            elif place[r][c] == 'X':
                Xlist.append([r,c])
    for i in range(len(plist)-1):
        for cp in range(i+1,len(plist)):
            if (abs(plist[i][0]-plist[cp][0])+abs(plist[i][1]-plist[cp][1]))<=2:
                if plist[i][0] == plist[cp][0]:
                    if plist[cp][1] - plist[i][1] == 1:
                        err = True
                        break
                    elif [plist[i][0],plist[i][1]+1] not in Xlist:
                        err = True
                        break
                elif plist[i][1] == plist[cp][1]:
                    if abs(plist[cp][0]-plist[i][0]) == 1:
                        err = True
                        break
                    elif [plist[i][0]+1 , plist[i][1]] not in Xlist:
                        err = True
                        break
                else:
                    if plist[cp][1] < plist[i][1]:
                        if ([plist[i][0]+1,plist[i][1]] not in Xlist) or ([plist[i][0],plist[i][1]-1] not in Xlist):
                            err = True
                            break
                    else:
                        if ([plist[i][0]+1,plist[i][1]] not in Xlist) or ([plist[i][0],plist[i][1]+1] not in Xlist):
                            err = True
                            break
    if err == True:
        return 0
    else:
        return 1

        
def solution(places):
    answer = []
    for m in places:
        answer.append(search_and_catch(m))
    return answer