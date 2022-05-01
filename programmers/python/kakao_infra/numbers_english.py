#https://programmers.co.kr/learn/courses/30/lessons/81301?language=python3
import string


number = {"one" : "1","two" : '2','three' : '3','four' : '4','five' : '5','six' : '6','seven' : '7', 'eight': '8' , 'nine' : '9' , 'zero' : '0'}

def solution(s):
    temp = ""
    for i in range(0,len(s)):
        if s[i] in number.values():
            temp +=s[i]
            continue
        else:
            if s[i:i+3] in number.keys():
                temp += number[s[i:i+3]]
                continue
            elif s[i:i+4] in number.keys():
                temp += number[s[i:i+4]]
                continue
            elif s[i:i+5] in number.keys():
                temp += number[s[i:i+5]]
                continue
    return int(temp)