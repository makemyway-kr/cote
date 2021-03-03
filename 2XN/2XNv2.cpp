#include <iostream>
using namespace std;
int answer = 0;
int fact(int n)
{
    if(n==0|| n==1)return 1;
    else return n*fact(n-1);
}
int permutation(int a,int b)//같은 것이 존재하는 순열로 풀었음.(고등학교 확통에 있음. 이걸로 푼 분은 근데 안보이는듯?)
{
    return fact(a+b)/(fact(a)*fact(b));
}
int solution(int n)
{
    if(n==0)return 0;
    if(n%2==0)
    {
        for(int i=n/2;i>=0;i--) //i is the number of set of horizontally stacked-rect
        {
            answer+=permutation(i,n-(i*2));
        }
    }
    else
    {
        for(int i=n/2;i>=0;i--)
        {
            answer+=permutation(i,n-(i*2)+1);
        }
    }
    return answer%1000000007;
}
int main()
{
    while(true)
    {
        int n=0;
        cin>>n;
        if(n==-1)break;
        cout<<solution(n)<<endl;
    }
}
