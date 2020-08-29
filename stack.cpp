#include <iostream>
#include <string>
using namespace std;
int N;
int* stack;
void push(int a)
{
	int i = 0;
	while (i<N)
	{
		if (stack[i] == NULL)
		{
			break;
		}
		else
		{
			i++;
		}
	}
	stack[i] = a;
}
int pop()
{
	int k = 0;
	while (k < N)
	{
		if (stack[k] == NULL)
		{
			break;
		}
		else
		{
			k++;
		}
	}
	if (k == 0)
	{
		return -1;
	}
	else
	{
		int j = stack[k - 1];
		stack[k - 1] = NULL;
		return j;
	}
}

int  size()
{
	int u = 0;
	while (u < N)
	{
		if (stack[u] == NULL)
		{
			break;
		}
		else u++;
	}
	return u;
}
int empty()
{
	if (stack[0] == NULL)
	{
		return 1;
	}
	else return 0;

}
int top()
{
	if (empty() == 1)return -1;
	else
	{
		int i = 0;
		while (i < N)
		{
			if (stack[i + 1] == NULL)
			{
				break;
			}
			else i++;
		}
		return stack[i];
	}
}
int main(void)
{
	cin >> N;
	stack = new int [N];
	for (int k = 0; k < N; k++)
	{
		stack[k] = NULL;
	}
	int i = 0;
	int num;
	string input;
	while (i<N)
	{
		cin >> input;
		if (input.compare("push") == 0)
		{
			cin >> num;
			push(num);
		}
		else if (input.compare("pop") == 0)
		{
			cout<<pop();
		}
		else if (input.compare("size") == 0)
		{
			cout<<size();
		}
		else if (input.compare("empty") == 0)
		{
			cout << empty();
		}
		else if (input.compare("top") == 0)
		{
			cout << top();
		}
	}
}