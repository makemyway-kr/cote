#include <string>
#include <vector>
#include <queue>
using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    vector<int> time;//완성 시간 vector
    for(int i=0;i<progresses.size();i++)
    {
        if((100-progresses[i])%speeds[i]==0)//나누어 떨어지는 경우
        {
            time.pushback((100-progresses[i])/speeds[i]);//시간 저장

        }
        else//나누어 떨어지지 않는 경우
        {
            time.pushback(((100-progresses[i])/spees[i])+1);
        }
    }
    while(!time.empty())
    {
        
    }
    return answer;
}
