def solution(gems):
    answer = []
    gemsl=set(gems)#보석종류 저장
    for ran in range(len(gemsl),len(gems)+1):#최소한 보석의 종류만큼은 사야함, 최대 진열장 모두
        for s in range(len(gems)-ran+1):#시작 위치
            temp=set(gems[s:s+ran])
            if len(temp)==len(gemsl):
                answer.append(s+1)
                answer.append(s+ran)
                break 
        if len(answer)!=0:
            break              
    return answer
print(solution(["DIA", "EM", "EM", "RUB", "DIA"]))