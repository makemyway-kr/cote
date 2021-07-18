def solution(name):
    answer = 0
    to_change=0
    for i in name:
        if i !='A':
            to_change+=1
    left=0
    right=0
    i=len(name)-1
    if name[0]!='A':
        left+=1
    while name[i]!='A':
        if name[i]!='A':
            left+=1
        if i==0:
            break
        i=i-1
    i=0
    while name[i]!='A':
        if name[i]!='A':
            right+=1
        if i==len(name)-1:
            break
        i=i+1
    return answer