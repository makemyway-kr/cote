#https://programmers.co.kr/learn/courses/30/lessons/17677?language=python3
import math
def splitter(tosplit):
    result = {}
    for i in range(0,len(tosplit)-1):
        temp = tosplit[i : i+2]
        if temp.isalpha() and temp.find(" ") == -1:
            if temp in result.keys():
                result[temp]+=1
            else:
                result[temp] = 1
    return result
def solution(str1, str2):
    answer = 0
    temp1 = str1.lower()
    temp2 = str2.lower()
    if temp1 == temp2:
        return 65536
    else:
        set1 = splitter(temp1)
        set2 = splitter(temp2)
        union = set1.copy()
        inter = {}
        for i in set2.keys():
            if i in union.keys():
                if set2[i]> union[i]:
                    union[i] = set2 [i]
            else:
                union[i] = set2 [i]
            if i in set1.keys():
                inter[i] = min(set1[i],set2[i])
        answer = int(math.floor(float(sum(inter.values()))/float(sum(union.values())) * 65536))
        return answer

print(solution("aa1+aa2" , "AAAA12"))