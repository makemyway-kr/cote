<h2>백준:RGB거리 문제</h2><br>
거진 2년만에 백준에서 문제를 풀었다.<br>
문제 해결과정보다는, 백준의 코드 제출 및 채점방식에 애를 먹었다.<br>
백준에서는 input값이 사용자 입력으로 주어지고, 출력 또한 print해주는 방식으로 해야한다.<br>
반면 프로그래머스에서는 주어진 함수로 input값이 매개변수로 입력되며, return해주는 방식으로 결과값을 전달한다.<br>
<br><br>
이 문제를 greedy방식을 이용하여 풀기를 시도하였지만, 코드가 너무 길어졌고 주어진 문제 설명에 DP를 이용하라는 설명이 있었다<br>
DP(dynamic programming)이란, 하나의 큰 문제를 여러개의 자잘한 문제(연산)으로 나누어 이를 해결하는 방식이다.<br>
알고리즘 문제 해결이 오랜만이어서 다시 공부하는 정도로 개념을 되살려 보고자 하였다.<br>
이 문제는 주어진 집들을 어떻게하면 최소 비용으로 앞뒤의 집들과 다른색으로 칠할수있냐를 구해야했다<br>
근데 이걸 단순히 생각하면, 앞에서부터 순서대로 그 앞집과 다른색으로 칠할 수 있는 최소의 비용을 구해나가기만 하면 된다<br>
예를 들어, 세채의 집을 칠해야 한다면, 2번집(부터) 빨간색, 파란색,초록색으로 칠한다면 각각의 색이 아닌 색으로 1번집을 칠하는 비용 중<br>
적은 비용을 R,G,B 색을 칠하는 비용에 더해주면 된다. 이렇게하면 2번집 빨간색-1번집 초록색(예시)의 비용이 2번집을 칠하는 비용에<br>
함께 들어있게 되고, 3번집을 R,G,B 세 색으로 칠하는 비용 또한 3번집을 파란색으로 칠한다 할때, 2번집이 빨간색일때의 비용이 가장 적다하면, <br>
3번집 파란색-2번집 빨간색-1번집 초록색의 비용이 3번집을 빨갛게 칠하는 데에 가장 최저의 비용으로 함께 계산되게 된다.
마지막으로 3번집을 칠하는 비용 중 가장 적은 비용을 고르면, 가장 적은 비용으로 세 채의 집을 칠하는 비용을 구할 수 있다.