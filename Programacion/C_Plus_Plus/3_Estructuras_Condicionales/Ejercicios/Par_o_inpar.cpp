#include<iostream>
using namespace std;

int main(int argc, char const *argv[])
{
	int n1;

	cout<<"Digite un numero el que quiera: ";cin>>n1;

	if (n1%2==0)
	{
		cout<<"El numero es par";
	}else{
		cout<<"El numero es impar";
	}
	return 0;
}