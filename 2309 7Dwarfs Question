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
				dwarfs[i] = -1;
				dwarfs[j] = -1;
				break;
			}
		}
	}
	for (int i = 0; i < 9; i++)
	{
		if (dwarfs[i] != -1)
		{
			cout << dwarfs[i] << endl;
		}
	}
    
}
   
