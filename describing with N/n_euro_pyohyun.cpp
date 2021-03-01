#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <set>
using namespace std;

int solution(int N, int number) {
    int answer = -1;
    int temp=0;
    vector<set<int>>numbers(9);//basic numbers
    for(int i=1;i<9;i++)
    {
        temp=(temp*10)+N;
        numbers[i].insert(temp);
    }
    for(int i=2;i<9;i++)
    {
        for(int j=1;j<i;j++)
        {
            int k=i-j;
            for(int m:numbers[j])
            {
                for(int n:numbers[k])
                {
                    numbers[i].insert(m+n);
                    if(m-n>0)numbers[i].insert(m-n);
                    numbers[i].insert(m*n);
                    if(m/n>=1)numbers[i].insert(m/n);
                }
            }
        }
        if(numbers[i].find(number)!=numbers[i].end())return i;
    }
   
    return answer;
}
int main(void)
{
    cout<<solution(5,12);
}
