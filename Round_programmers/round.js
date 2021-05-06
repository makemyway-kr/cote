function solution(n,a,b)
{
    var answer = 1;
    while(answer<=n && a>=1 && b>=1)
    {
        if((a%2==1)&&(b%2==0)&&b==a+1||(b%2==1)&&(a%2==0)&&a==b+1)//a가 홀수번, b가 짝수이고 둘의 차가 1(붙어있음)이거나  a가 짝수이고 b가 홀수(이때는 a가 b보다 1큰 경우여야함.)
        {
            break;
        }
        else
        {
            if(a%2==0)
            {
                a=a/2;
            }
            else if(a%2==1)
            {
                if(a!=1)
                {
                    a=(a+1)/2;
                }
                
            }
            if(b%2==0)
            {
                b=b/2;
            }
            else if(b%2==1)
            {
                if(b!=1)
                {
                    b=(b+1)/2;
                }
            }
            answer++;
        }
        
    }
    return answer;
}    