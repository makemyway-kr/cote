def solution(jobs):
    answer = 0
    time_list=[]
    currtime=0
    while(len(jobs)!=0):
        temp=1001
        tindex=0
        for i in range(len(jobs)):
            if jobs[i][1]<temp and jobs[i][0]<=currtime:
                temp=jobs[i][1]
                tindex=i
        if temp==1001:
            currtime+=1
        else:
            time_list.append([tindex,(currtime-jobs[tindex][0])+jobs[tindex][1]])
            del jobs[tindex]
            currtime+=temp
    for k in range(len(time_list)):
        answer=answer+time_list[k][1]
    answer=answer/len(time_list)
    return int(answer)