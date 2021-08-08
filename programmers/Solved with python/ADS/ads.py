#https://programmers.co.kr/learn/courses/30/lessons/72414#
def solution(play_time, adv_time, logs):
    answer=''
    answer_pool=[]
    if play_time==adv_time:
        answer="00:00:00"
    else:
        adv=adv_time.split(':')
        advtimetosec=(3600*(int(adv[0])))+(60*int(adv[1]))+int(adv[2])
        logs_div=[]
        logs_by_second=[]
        for i in logs:
            temp=i.split('-')
            for k in temp:
                logs_div.append(k.split(':'))
        temp=[]
        for i in range(len(logs_div)):
            temp_second=0
            for j in range(3):
                if j==0:
                    temp_second+=3600*int(logs_div[i][j])    
                elif j==1:
                    temp_second+=60*int(logs_div[i][j])
                else:
                    temp_second+=int(logs_div[i][j])
                    temp.append(temp_second)
            if((i%2)==1):
                logs_by_second.append(temp)
                temp=[]
        logs_by_second.sort(key=lambda logs_by_second:logs_by_second[0])
        while(len(answer_pool)!=len(logs_by_second)):
            curr=len(answer_pool)
            tem_start=logs_by_second[curr][0]
            tem_fin=tem_start+advtimetosec
            count_up=min(logs_by_second[curr][1]-logs_by_second[curr][0],advtimetosec)
            for i in range(curr+1,len(logs_by_second)):
                    if logs_by_second[i][0]<=tem_fin:#광고 종료 예정 시간 전에 시작하는 로그
                        if logs_by_second[i][1]<=tem_fin:#광고 종료 전에 해당 로그(시청)이 끝나면
                            count_up+=logs_by_second[i][1]-logs_by_second[i][0]
                        else:
                            count_up+=tem_fin-logs_by_second[i][0]               
                    else:
                        break
            answer_pool.append([count_up,tem_start])
        answer_pool.sort(key=lambda answer_pool:(-answer_pool[0],answer_pool[1]))
        hour=answer_pool[0][1]//3600
        minutes=(answer_pool[0][1]%3600)//60
        sec=(answer_pool[0][1]%3600)%60
        if hour//10<1:
            hour="0"+str(hour)
        else:
            hour=str(hour)
        if minutes//10<1:
            minutes="0"+str(minutes)
        else:
            minutes=str(minutes)
        if sec//10<1:
            sec="0"+str(sec)
        else:
            sec=str(sec)
        answer=hour+':'+minutes+':'+sec
        print(answer)
    return answer
solution("02:03:55","00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])