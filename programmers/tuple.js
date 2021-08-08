function solution(s) {
    var answer = [];
    var temper = [];
    var temp = "";
    for (var i = 0; i < s.length; i++) {
        if (s[i] != "{" && s[i] != "}") {
            temp += s[i];
        } 
        else if (s[i] == "}" && i != s.length - 1) {
            temper.push(temp);
            i=i+1;
            temp="";
        }
    } //{}단위로 넣음.

    var temper2 = [];
    for (var i = 0; i < temper.length; i++) {
        temp = "";
        var tempin = [];
        for (var k = 0; k < temper[i].length; k++) {
            if (temper[i][k] != ',') {
                temp += temper[i][k];
            } else if (temper[i][k] == ',') {
                tempin.push(Number(temp));
                temp = "";
            }
        }
        tempin.push(Number(temp));
        temper2.push(tempin);
    }
    for (var i = 0; i < temper2.length; i++) {
        for (var k = 0; k < temper2.length; k++) {
            if (temper2[k].length == i + 1) {
                for (var l = 0; l < temper2[k].length; l++) {
                    if (answer.indexOf(temper2[k][l]) == -1) {
                        answer.push(temper2[k][l]);
                    }
                }
            }
        }
    }
    return answer;
}