def solution(gems):
    answer=[]
    gemlist=set(gems)
    pool=[]
    direct_key=0
    for start in range(0,len(gems)-len(gemlist)):
        for length in range(len(gemlist),len(gems)+1):
            if len(set(gems[start:start+length]))==len(gemlist):
                pool.append([start+1,start+length,length])
                if length==len(gemlist):
                    answer.append(start+1)
                    answer.append(start+length)
                    direct_key=1
                    break
        if direct_key==1:
            break
    if direct_key!=1:
        pool.sort(key=lambda pool:pool[2])
        answer=[pool[0][0],pool[0][1]]
    return answer
solution(["XYZ", "XYZ", "XYZ"])