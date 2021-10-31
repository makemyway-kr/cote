//프로그래머스 이중우선순위큐 (level3)문제
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <list>
using namespace std;

vector<int> solution(vector<string> operations) {
    list <int> templist;
    int ittime=operations.size();
    for(int i=0;i<ittime;i++)
    {
        string temp=operations.front();
        if(temp[0]=='I'){
            int tempnum=stoi(temp.substr(2,temp.length()-2));
            templist.push_back(tempnum);
        }
        else{
            if(templist.size()!=0){
                if(temp.find('-')<temp.size()){
                    templist.sort();
                    templist.pop_front();
                    
                }
                else{
                    templist.sort();
                    templist.pop_back();
                }
            }
            
        }
        operations.erase(operations.begin());
    }
    vector<int> answer;
    if(templist.empty()){
        answer.push_back(0);
        answer.push_back(0);
    }
    else{
        templist.sort();
        answer.push_back(templist.back());
        answer.push_back(templist.front());
    }
    return answer;
}