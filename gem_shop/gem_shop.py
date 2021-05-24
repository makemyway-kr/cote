import copy
def solution(gems):
    answer = []
    tempan=1000001
    gemsl=[]#보석 종류 저장 list
    for i in gems:
        if i not in gemsl:
            gemsl.append(i)
    for ran in range(len(gemsl),len(gems)+1):#최소한 보석의 종류만큼은 사야함, 최대 진열장 모두
        for s in range(len(gemsl)):#시작 위치
            tempg=copy.deepcopy(gemsl)
            lister=copy.deepcopy(gems[s:s+ran])
            rlist=[]
            for k in lister:
                if k in tempg:
                    tempg.remove(k)
                    rlist.append(k)
            if len(tempg)==0 and ran<tempan:
                tempan=ran
                answer.clear()
                answer.append(s+1)
                answer.append(s+ran)
    return answer
print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))