function solution(s) {
    var answer = [];
    for(var i=0;i<s.length;i++)
    {
        var temp;
        if(s[i]!='{' && s[i]!='}' && s[i]!=','){
           temp+=s[i];
        }
        if(s[i]==','){
            var count=0;
            for(var j=0;j<answer.length;j++){
                if(answer[j]==Number(temp)){
                    count+=1;
                }
            }
            if(count==0){
                answer.push(Number(temp));
            }
        }
    }
    return answer;
}