using namespace std;

int solution(int n) {
    int answer = 2;
    int temp=1;
    int before=1;
    for(int i=3;i<=n;i++)
    {
        temp=answer;
        answer=answer+before;
        before=temp;
        answer=answer%1000000007;
    }
    return answer;
}
