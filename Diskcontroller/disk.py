def solution(jobs):
    answer = 0
    time_list=[]
    currtime=0
    while(len(jobs)!=0):#남는 일이 없을때까지
        temp=1001#소요시간
        tindex=0#job의 인덱스번호 저장
        for i in range(len(jobs)):#현재 시간보다 이전, 또는 방금 들어온 작업들 중에서, 소요시간이 가장 적은것을 수행하도록함.
            if jobs[i][1]<temp and jobs[i][0]<=currtime:
                temp=jobs[i][1]
                tindex=i
        if temp==1001:# 현재 들어온 작업이 없어 temp값이 그대로 1001로 있을 경우 시간을 흐르게 한다.
            currtime+=1
        else:#수행할 작업(가장 짧은 작업)이 있는 경우
            time_list.append([tindex,(currtime-jobs[tindex][0])+jobs[tindex][1]])#요청시간부터 수행마무리한 시간까지를 계산하여 list에 넣음
            del jobs[tindex]#기존 일 목록에서 삭제함
            currtime+=temp
    for k in range(len(time_list)):#평균 구하기
        answer=answer+time_list[k][1]
    answer=answer/len(time_list)
    return int(answer)