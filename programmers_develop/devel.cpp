#include <string>
#include <vector>
using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    vector<int> time;//완성 시간 vector
    for(int i=0;i<progresses.size();i++)//완성까지의 시간 계산
    {
        if((100-progresses[i])%speeds[i]==0)//나누어 떨어지는 경우
        {
            time.push_back((100-progresses[i])/speeds[i]);//시간 저장

        }
        else//나누어 떨어지지 않는 경우
        {
            time.push_back(((100-progresses[i])/speeds[i])+1);
        }
    }
    int remaining=time.size();
    while(remaining!=0)
    {
        int count=1;
        for(int i=time.size()-remaining+1;i<time.size();i++)
        {
            if(time[i]<=time[time.size()-remaining])
            {
                count++;
            }
            else
            {
                break;
            }
        }
        remaining-=count;
        answer.push_back(count);
    }
    return answer;
}
