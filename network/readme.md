<h2>프로그래머스::네트워크 문제 with python</h2><br>

<br>
문제 설명: 깊이우선 탐색을 사용하여 컴퓨터의 갯수와 컴퓨터간의 연결 여부가 주어졌을때, 전체 네트워크 망의 갯수를 구하라<br>
그런데 이때, 1번/2번 컴퓨터가 연결되어있고 2번/3번 컴퓨터가 연결되어있으면 1,2,3은 하나의 네트워크 이다 라고 한다.<br>
그리고 다른 컴퓨터와 연결이안된 4번 컴퓨터가 있다 할때, 이는 네트워크 하나를 한개의 컴퓨터가 이루고 있는 것이라고 정의한다고 문제는 말한다.<br>
<br>
<h4>이 문제에서 사용한 알고리즘/함수</h4>
<ol>
  <li>DFS(깊이 우선 탐색)</li>
  우선 하나의 컴퓨터를 가지고 연결되어있는 컴퓨터의 끝까지 쭉 탐색한 뒤, (재귀함수를 이용) 다시 시작점으로 돌아오면 하나의 네트워크를 찾게 되는 것이다.
</ol>
<br>
위에서도 설명하였듯이, 재귀함수를 이용해서 solution함수에서는 0번부터 n-1번까지 컴퓨터중 앞의 컴퓨터와 연결되어있는 컴퓨터를 제외한 컴퓨터의 네트워크를 탐색하도록<br>
반복문을 실행한다. 그리고 DFS(깊이우선 탐색) 함수가 계속 돌아가며 연결되어있는 컴퓨터를 확인하고, 연결을 확인한 컴퓨터는 queue에 넣어주었다.<br>
이렇게 해서 다시 끝까지 갔다가 돌아오게되면(설령 하나도 연결되어있지 않더라도) 네트워크 하나를 찾아낸 것으로 answer값을 증가시켜준다.
<br>
이 문제를 해결하기 전 썼던 코드를 첨부해본다.(배운 내용이 있음)

 import copy<br>
queueofconnected=[]<br>
num_of_com=0<br>
comlans=[]<br>
def dfs(num,lan):<br>
        queueofconnected.append(num)<br>
        for k in range (num_of_com):<br>
            if lan[k]==1 and k!=num:<br>
                if k not in queueofconnected:<br>
                    dfs(k,comlans[k])<br>
<br>
            <br>
def solution(n, computers):<br>
    answer = 0<br>
    num_of_com=n<br>
    comlans=copy.deepcopy(computers)<br>
    for i in range (n):<br>
        if i not in queueofconnected:<br>
            dfs(i,comlans[i])<br>
            answer+=1<br>
    return answer<br>
<br>
여기서는 copy를 이용해서 전역변수에 컴퓨터의 연결여부 2차원배열과 컴퓨터의 갯수를 저장하여 사용하려 하였으나,<br>
파이썬에서는 전역변수를 함수 안에서 수정하려면 global을 써주어야한다는 것을 몰라, 계속해서 오류가 났다.
<br>
그래서 계속해서 함수 안의 num_of_com은 선언조차도 안해주었으니 없는 변수를 for반복문에 써준것이나 다름 없었고,
<br>
오류가 발생했다.
