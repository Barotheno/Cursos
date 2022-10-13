#include<iostream>

using namespace std;

int main(int argc, char const *argv[])
{
	float n1,n2,n3;

	cout<<"Introduzca los tres números separados por un espacio: ";cin>>n1>>n2>>n3;

	if ((n1 > n2) && (n1 > n3))
	{
		cout<<"El numero mayor es: "<<n1;
	}else if ((n2 > n1) && (n2 > n3))
	{
		cout<<"El numero mayor es: "<<n2;
	}else if ((n3 > n1) && (n3 > n2))
	{
		cout<<"El numero mayor es: "<<n3;
	}else{
		cout<<"Son iguales";
	}


	return 0;
}