def solution(gems):
    answer=[]
    gemlist=set(gems)
    key=0
    for length in range(len(gemlist),len(gems)+1):
        for start in range(0,len(gems)+1):
            if len(set(gems[start:start+length]))==len(gemlist):
                answer.append(start+1)
                answer.append(start+length)
                key=1
                break
        if key==1:
            break
    return answer
solution(["XYZ", "XYZ", "XYZ"])