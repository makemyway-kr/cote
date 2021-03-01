#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int solution(int N, int number) {
    int answer = -1;
    int temp=0;
    vector<vector<int>>numbers;//basic numbers
    for(int i=0;i<8;i++)
    {
        temp=temp*10+N;
        numbers[i].push_back(temp);
    }
    for(int i=0;i<8;i++)
    {
        for(int u=8-i-2;u>=0;u--)
        {
            for(int k=0;k<numbers[i].size();k++)
            {
                for(int j=0;j<numbers[u].size();j++)
                {
                    numbers[i+u+1].push_back(numbers[i][k]+numbers[u][j]);
                    numbers[i+u+1].push_back(numbers[i][k]-numbers[u][j]);
                    numbers[i+u+1].push_back(numbers[i][k]*numbers[u][j]);
                    if(numbers[i][k]/numbers[u][j]>=1)numbers[i+u+1].push_back(numbers[i][k]/numbers[u][j]);
                }
            }
        }
    }
    for(int i=0;i<8;i++)
    {
        if(find(numbers[i].begin(),numbers[i].end(),number)!=numbers[i].end())answer=i;
    }
    return answer;
}
