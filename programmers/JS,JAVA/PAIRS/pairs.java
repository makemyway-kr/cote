//프로그래머스 짝지어제거하기
import java.lang.*;
import java.util.Stack;
class Solution
{
    public int solution(String s)
    {
        int answer = 0;
        Stack<Character> deletestack=new Stack<>();
        for(int i=0;i<s.length();i++)
        {
            char latest=s.charAt(i);
            if(!deletestack.empty()&& deletestack.peek()==latest)
            {
                deletestack.pop();
            }
            else
            {
                deletestack.push(latest);
            }
        }
        if(deletestack.empty())
        {
            answer=1;
        }
        return answer;
    }
}