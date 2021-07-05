def solution(gems):
    answer=[]
    gemlist=set(gems)
    pool=[]
    for start in range(0,len(gems)-len(gemlist)+1):
        for length in range(len(gemlist),len(gems)-start+1):
            if len(set(gems[start:start+length]))==len(gemlist):
                pool.append([start+1,start+length,length])
                if length==len(gemlist):
                    answer.append(start+1)
                    answer.append(start+length)
                break
    pool.sort(key=lambda pool:pool[2])
    answer=[pool[0][0],pool[0][1]]
    print(answer)
    return answer