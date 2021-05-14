//프로그래머스 입국심사
function solution(n, times) {
    var time = 0;
    var people = n;
    var officers = new Array(times.length);
    for (var i = 0; i < times.length; i++) {
        officers[i] = false; //업무중이 아니면 false
    }
    while (people > -times.length) {
        for (var i = 0; i < times.length; i++) {
            if (officers[i] == false) {
                people -= 1;
                officers[i] = true;
            } else if (officers[i] == true && time % times[i] == 0) { //현재 시간을 소요시간으로 나누어 떨어지면 일이 끝남. 새 사람 받음.
                people -= 1;
            }

        }
        time++;
    }
    time -= 1; //제일 마지막에도 시간이 증가하므로 하나 빼줘야함.
    return time;
}