def solution(gems):
    answer = []
    start=0
    gemsl=set(gems)#보석종류 저장
    end=start+len(gemsl)-1
    length=100001
    glen=len(gems)
    gtype=len(gemsl)
    while start<=glen-gtype and end<glen:
        if len(set(gems[start:end+1]))==gtype and end-start<length:
            length=end-start
            answer.clear()
            answer.append(start+1)
            answer.append(end+1)
        if end==len(gems)-1 and start!=len(gems)-1:
            start+=1
            end=start+len(gemsl)-1
        else:
            end+=1
    return answer
print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))