#include <stdio.h>
#include <iostream>

using namespace std;

int main()
{
	int num;
	cin >> num;
	if (num < 10)
	{
		cout << "This number<10" << endl;
	}
	else
	{
		cout << "This number >=10" << endl;
	}
	return 0;
}
