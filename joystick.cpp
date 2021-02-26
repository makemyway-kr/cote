#include <string>
#include <vector>
#include <iostream>
using namespace std;

int solution(string name) {
    int answer = 0;
    int modify_1=name.length();
    int modify_2=name.length();
    for(int i=0;i<name.length();i++)//수정해야하는 칸 갯수 구해두기
    {
        if(name[i]=='A')
        {
            modify_1-=1;
            modify_2-=1;
        }
    }
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
            modify_1-=1;
        }
        if(!((i==name.length()-1)||(modify_1==0)))answer+=1;//이름을 다 고쳤거나 남은것이 모두 A이면 키를 조작하지 않음.
        if(modify_1==0)break;//더이상 수정할 글자가 없으면 끝.
        
    }
    int t=0;//첫 위치에서 뒤로 돌아서 이름을 수정할 때의 경우
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
        modify_2-=1;
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
            modify_2-=1;
        }
        if(!((i==1 )|| modify_2==0))t+=1;
        if(modify_2==0)break;
    }
    if(t<answer)answer=t;
    
    return answer;
}
int main()
{
    cout<<solution("JAZ");
}
