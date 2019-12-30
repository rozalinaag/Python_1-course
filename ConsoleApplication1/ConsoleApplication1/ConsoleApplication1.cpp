#include <stdio.h>
#include <iostream>
using namespace std;


int main()
{
	cout<<"What do you want to see today ? \n";
	
	cout<<"1 - Wave\n";
	cout<<"2 - Arrow\n";
	cout<<"3 - Supernatural\n";
	cout<<"4 - Exit\n";
	
	cout<<"Your choise: ";
	
	int input; //наше число 1,2,3 или 4

	cin>>"%d", &input; //вводи числа 
	
	switch (input) //оператор выбора
	{
	case 1:			//обратить внимание на двоеточие
		cout<<"<<His Death Was Just The Beginning";
		break;
	case 2:
		cout<<"<<Scary Just Got>>\n";
		break;
	case 3:
		cout<<"<<Fight the dead.>>\n";
		break;
	case 4:
		cout<<"go to sleep\n";
		break;
	default:
		cout<<"can you count to 4?\n";
	}

	return 0;
}

