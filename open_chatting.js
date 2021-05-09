function solution(record) {
    var listoflog = new Array(record.length);
    for (var i = 0; i < record.length; i++) {
        listoflog[i] = record[i].split(' ');
    }
    var iddict = {};
    for (var i = 0; i < record.length; i++) {
        if (listoflog[i][0] == "Enter") {
            iddict[listoflog[i][1]] = listoflog[i][2];
        } else if (listoflog[i][0] == "Change") {
            iddict[listoflog[1][1]] = listoflog[i][2];
        }
    }
    var answer = [];
    for (var i = 0; i < record.length; i++) {
        if (listoflog[i][0] == "Enter") {
            var tempstring = iddict[listoflog[i][1]] + "님이" + " 들어왔습니다.";
            answer.push(tempstring);
        } else if (listoflog[i][0] == "Leave") {
            var tempstring = iddict[listoflog[i][1]] + "님이 " + "나갔습니다.";
            answer.push(tempstring);
        }
    }
    return answer;
}