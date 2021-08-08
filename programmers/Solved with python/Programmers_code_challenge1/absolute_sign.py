def rotate(s,n):#getting string and times of rotation
    temp=[]
    temp2=[]
    for j in range (n):
        temp.append(s[j])
    for j in range(n,len(s)):
        temp2.append(s[j])
    for j in range(len(temp)):
        temp2.append(temp[j])
    return temp2
    
def if_right(s):#각각의 괄호 배열에 괄호의 위치들을 추가함. 괄호의 갯수가 동일하지 않거나 오른쪽 괄호( ")" 등)이 왼쪽 괄호보다 먼저나오면 완벽한 괄호문장이아님.
    ans=True
    bigflag=[[],[]]
    midflag=[[],[]]
    smallflag=[[],[]]
    for k in range(len(s)):
        if s[k]=="(":
            smallflag[0].append(k)
        elif s[k]==")":
            smallflag[1].append(k)
        elif s[k]=="{":
            midflag[0].append(k)
        elif s[k]=="}":
            midflag[1].append(k)
        elif s[k]=="[":
            bigflag[0].append(k)
        elif s[k]=="]":
            bigflag[1].append(k)
    if len(smallflag[0])!=len(smallflag[1]) or len(midflag[0])!=len(midflag[1]) or len(bigflag[0])!=len(bigflag[1]):
        ans=False
    else:
        for k in range(len(smallflag[0])):
            if smallflag[0][k]>smallflag[1][k]:
                ans=False
               
        for k in range(len(midflag[0])):
            if midflag[0][k]>midflag[1][k]:
                ans=False
                
        for k in range(len(bigflag[0])):
            if bigflag[0][k]>bigflag[1][k]:
                ans=False
                
    return ans
    
def solution(s):
    answer = 0
    if if_right(s)==True:
        answer+=1
    for i in range(1,len(s)):
        if if_right(rotate(s,i))==True:
            answer+=1
            
    return answer