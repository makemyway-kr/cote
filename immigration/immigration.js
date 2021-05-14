//프로그래머스 입국심사
function solution(n, times) {
    var ltime = 0;
    ltime = 1; //왼쪽끝
    var sumt = [];
    var rtime = Math.max(...times) * n; //오른쪽
    var time = rtime; //계산 대상 시간
    while (ltime <= rtime) {
        if (n == times.length) {
            sumt.push(Math.max(...times));
            ltime = rtime + 1;
            break;
        } else {
            var temp = new Array(times.length);
            for (var i = 0; i < times.length; i++) {
                temp[i] = Math.floor(time / times[i]);
            }
            var ssum = temp.reduce(function add(tsum, currvalue) {
                return tsum + currvalue;
            }, 0);
            if (ssum >= n) {
                if (ssum == n) {
                    sumt.push(time);
                }
                rtime = time - 1;
                time = Math.floor((ltime + rtime) / 2);
            } else if (ssum < n) {
                ltime = time + 1;
                time = Math.floor((ltime + rtime) / 2);
            }

        }

    }
    return Math.min(...sumt);
}