#include<iostream>
using namespace std;

int main(int argc, char const *argv[])
{
	int n1;

	cout<<"Digite su edad: ";cin>>n1;

	if ((n1 >= 18) && (n1 <= 25))
	{
		cout<<"Su rango de edad esta dentro de los 18 y 25 años";
	}else{
		cout<<"Su rango de edad está fuera de lo permitido";
	}

	return 0;
}