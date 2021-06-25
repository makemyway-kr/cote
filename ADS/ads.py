#https://programmers.co.kr/learn/courses/30/lessons/72414#
def solution(play_time, adv_time, logs):
    answer = ''
    play=play_time.split(':')
    adv=adv_time.split(':')
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
            print(temp)
            logs_by_second.append(temp)
            temp=[]
    print(logs_by_second)
    return answer
solution("02:03:55","00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])