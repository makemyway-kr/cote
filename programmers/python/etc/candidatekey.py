#lv2 후보키
from itertools import combinations
def solution(relation):
    answer = 0
    nonUniqueColumns = []
    rows = len(relation)
    for c in range(len(relation[0])):
        temp = []
        for r in relation:
            temp.append(r[c])
        temp = set(temp)
        if len(temp) != rows:
            nonUniqueColumns.append(c)
        else:
            answer += 1
    keys = []
    for i in range(2,len(nonUniqueColumns)+1):
        for t in list(combinations(nonUniqueColumns,i)):
            temp = []
            for r in relation:#모든 row들에 대하여
                ct = []
                for rt in t: #column값들 뽑음
                    ct.append(r[rt])
                if ct not in temp:
                    temp.append(ct)
            isKey = False
            if len(temp) == rows:
                isKey = True
                for k in keys:
                    if set(k).issubset(set(t)): #최소성 파악
                        isKey = False
                        break
            if isKey == True:
                answer += 1
                keys.append(t)            
    return answer