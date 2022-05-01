#프로그래머스 표 편집 문제 https://programmers.co.kr/learn/courses/30/lessons/81303
def solution(n, k, cmd):
    #n은 전체 행 개수,k는 현재 선택 행 번호
    answer = ['O'for i in range(n)]
    undeleted=[i for i in range(0,n)]
    deleted=[]
    curr=k
    for command in cmd:
        c=command.split(' ')
        if c[0]=='U' or c[0]=='D':
            if c[0]=='U':
                curr-=int(c[1])
            else:
                curr+=int(c[1])
        elif c[0]=='C':
            answer[undeleted[curr]]='X'
            deleted.append([undeleted[curr],curr])#내용,위치
            undeleted.pop(curr)
            if curr==len(undeleted):
                curr=len(undeleted)-1
        elif c[0]=='Z':
            temp=deleted.pop()
            undeleted.insert(temp[1],temp[0])
            answer[temp[0]]='O'
            if temp[0]<=curr:#현재 위치 보다 앞에 복구가되면 인덱스가 하나 밀려야 맞음.
                curr+=1
    return ''.join(answer)