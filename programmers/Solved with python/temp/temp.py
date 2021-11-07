def solution(rows, columns):
    answer = [[0 for col in range(columns)]for row in range(rows)]
    curr=[0,0]
    prevnum=0
    visitiednum=0
    while visitiednum<rows*columns:#숫자를 채울 칸이 0이거나 행렬에 0이 있으면 계속함
        print(curr)
        if answer[curr[0]][curr[1]]!=0:
            if (answer[curr[0]][curr[1]]%2==0 and (prevnum+1)%2==0) or (answer[curr[0]][curr[1]]%2==1 and (prevnum+1)%2==1):#이미 적혀있는 숫자와 이제 쓸 숫자의 2로 나눈 나머지가 같으면 전의 경로를 그대로 따라가게됨
                break
        else:
            visitiednum+=1
        answer[curr[0]][curr[1]]=prevnum+1
        prevnum+=1
        if prevnum%2==0:
            curr[0]+=1
            if(curr[0]>=rows):
                curr[0]=0
        else:
            curr[1]+=1
            if(curr[1]>=columns):
                curr[1]=0
    return answer
print(solution(3,3))