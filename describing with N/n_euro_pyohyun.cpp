#include <string>
#include <vector>

using namespace std;

int solution(int N, int number) {
    int answer = -1;
    int temp=0;
    vector<vector<int>>numbers;
    for(int i=0;i<8;i++)
    {
        temp=temp*10+N;
        numbers[i].push_back(temp);
    }
    return answer;
}