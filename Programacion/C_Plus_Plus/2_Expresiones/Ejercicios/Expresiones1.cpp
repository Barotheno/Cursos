// Escribe la siguiente expresion en c++
// "a/b" + 1

#include<iostream>
using namespace std;

int main(int argc, char const *argv[])
{
	float a=0, b=0, total;

	cout<<"Digite el número a: ";cin>>a;
	cout<<"\nDigite el número b: ";cin>>b;

	total = (a/b) + 1;

	cout.precision(2);//Establecemos el maximo de decimales

	cout<<"El total es: "<<total;

	return 0;
}