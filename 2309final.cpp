#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
	int dwarfs[9];
	for (int i = 0; i < 9; i++)
	{
		cin >> dwarfs[i];
	}
	int sum = 0;
    int a=0;
    int b=0;
	for (int i = 0; i < 9; i++)
	{
		sum = sum + dwarfs[i];
	}
	sort(dwarfs, dwarfs + 9);
	for (int i = 0; i < 9; i++)
	{
		for (int j = i + 1; j < 9; j++)
		{
			if (sum - dwarfs[i] - dwarfs[j] == 100)
			{
				a=i;
                b=j;
				break;
			}
		}
	}
	for (int i = 0; i < 9; i++)
	{
		if (i!=a && i!=b)
		{
			cout << dwarfs[i] << endl;
		}
	}
    
}
   
