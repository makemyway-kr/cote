#include <string>
#include <vector>
#include <iostream>
using namespace std;

int solution(string name) {
    int answer = 0;
    for(int i=0;i<name.length();i++)
    {
        
        if(name[i]!='A')
        {
            if(name[i]-'A'>13)
            {
                answer+=(1+('Z'-name[i]));
            }
            else
            {
                answer+=(name[i]-'A');
            }
        }
        if(!((i==name.length()-1)||(i==name.length()-2 && name[i+1]=='A')))answer+=1;
        
    }
    int t=0;
    if(name[0]!='A')
    {
        if(name[0]-'A'>13)
        {
            t+=(1+('Z'-name[0]));
        }
        else
            {
                t+=name[0]-'A';
            }
    }
    t+=1;
    for(int i=name.length()-1;i>0;i--)
    {
        if(name[i]!='A')
        {
            if(name[i]-'A'>13)
            {
                t+=(1+('Z'-name[i]));
            }
            else
            {
                t+=name[i]-'A';
            }
        }
        if(!((i==1 )|| (i==2 && name[i-1]=='A')))t+=1;
    }
    if(t<answer)answer=t;
    
    return answer;
}
int main()
{
    cout<<solution("JAZ");
}
