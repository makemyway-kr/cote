<!---문제 설명--->

<h2>프로그래머스 :: N으로만 표현하기</h2><br>

사용언어:C++<br>
얻어간 지식: for문 안에 "int형 변수 : int 배열"의 형태로 하면 배열의 각 요소를 지나가며 변수에 담을 수 있다라는 것을 배웠다<br>

문제 설명: number(구하고 싶은 숫자)와 N(1~9사이)가 주어졌을때, 어떻게 하면 N만으로 number를 사칙연산의 형태로 표현할 수 있을까?<br>
그 중에서도 가장 N이라는 숫자를 적게 사용하면서 나타낼 수 있는 경우는 몇번 쓴 경우일까?<br>되시겠다.<br>

이때, N이 5라 하면 5/55/555....를 사용해서 number를 나타내는 것이다.<br>
입출력 예시:12 = 5 + 5 + (5 / 5) + (5 / 5)<br>
12 = 55 / 5 + 5 / 5<br>
12 = (55 + 5) / 5<br>
이때 답은 4 되겠죠?<br>

<br>
생각한 해결법:<h3>하나만 사용할 경우, 두개 사용할경우...해서 쭉쭉쭉 동적 프로그래밍의 방식을 사용하자!</h3><br>
간단하다. 우선 최소 경우가 8을 넘으면 -1을 return하라는 문제의 조건이 있었다. 그러므로 5부터 55555555까지를 일단 8행짜리 2차원 배열의 1열에 넣어둔다<br>
그 다음, 1행부터 8행까지 각 숫자를 서로 +/-/%/* 의 사칙연산을 시켜가며 구하고자 하는 숫자가 나오면 answer에 반영시킨다.<br>

가장 위의 i변수가 사용되는 N의 갯수를 통제하고, j/k를 이용하여 j+k==i를 만족시키는, ex)N이 2개쓰인 숫자, N이 3개 쓰인 숫자를 연산함, i==5라면.<br>
각 경우의 수를 연산시키며 i행의 배열을 채워나가는 것이다.<br>
