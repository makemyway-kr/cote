#include <string>
#include <vector>
#include <iostream>
using namespace std;
int answer = 0;
const int height_rect=2;
const int width=2;
const int height=1;
int solution(int n) {//n means left width to fill in my solution
    if(n==0)//if there's no left width to fill
    {
        answer++;
        return 0;
    }
    else if(n<0)return 0;//width overflowed
    solution(n-2);//filled with two rectangles horizontally
    solution(n-1);//filled with one rectangle vertically
    return answer;
}
