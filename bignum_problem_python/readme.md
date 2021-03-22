<h2>프로그래머스 가장 큰 수 문제 in Python</h2><br>
<br>
I originally solved this problem with kind of bubbles sorting<br>
As you can see in bignum.py, Using comapring function I compared each case of making new number with two different numbers at row<br>
It was quite fascinating way but there was time out problem with this<br>
So I googled about how to comparing two different numbers with different digits.<br>
Well, there was Idea to change int into string and make those two numbers over 3digits<br>
Because there was the condition that numbers cannot exceed 1000 in the question<br>
And also when computer compares two different strings, it compares differently from the way it compares numbers<br>
By changing each characters into AscII code number, it compares it ASCII code number from the beginning of the string<br>
So I used that and also by using lambda, I can change numbers' digits after changing them into string<br>
If I use lambda x: x*3 , it becomes xxx. So I can compare one-digit number with two/three digit numbers and in the end, <br>
I can conclude which number have to come front to make bigger number<br>
ex) if I compare 6 with 63, I compare 666 with 636363 and by Ascii code comparison, I can conclude that 6 has to come front.<br>
And also, 663 is bigger(when 6 comes front) than 636(when 63 comes front).
<br>
<br>
I currently decided to solve algorithm questions with python. (For using django or other web-programming skills).<br>

It is 2years ago that I lastly used python, so now I'm learning how to use Python.
