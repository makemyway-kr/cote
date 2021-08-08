import java.lang.Math;

import javax.lang.model.util.ElementScanner14;
class Solution {
    int answer = 0;
    int t=0;
    void DFS(int []numbers,int curr,int currstate){
        int cal1=curr;
        int cal2=curr;
        if(currstate<numbers.length)
        {
            for(int j=currstate;j<numbers.length;j++)
            {
                cal1=cal1+numbers[j];
                cal2=cal2-numbers[j];
            }
            if(curr<t && cal1>=t){
                DFS(numbers,curr+numbers[currstate],currstate+1);
                DFS(numbers,curr-numbers[currstate],currstate+1);
            }
            else if(curr>t && cal2<=t){
                DFS(numbers,curr+numbers[currstate],currstate+1);
                DFS(numbers,curr-numbers[currstate],currstate+1);
            }
            else if(curr==t){
                DFS(numbers,curr+numbers[currstate],currstate+1);
                DFS(numbers,curr-numbers[currstate],currstate+1);
            }
        }
        else if(currstate==numbers.length)
        {
            if(curr==t)
            {
                answer+=1;
            }
        }
        
    }
    public int solution(int[] numbers, int target) {
        t=target;
        DFS(numbers,numbers[0],1);
        DFS(numbers,-numbers[0],1);
        return answer;
    }
}