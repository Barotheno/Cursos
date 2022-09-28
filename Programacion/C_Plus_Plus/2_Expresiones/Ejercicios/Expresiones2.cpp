// Escribir la siguiente expresión: 
// a + b / c + d

#include<iostream>
using namespace std;

int main(int argc, char const *argv[])
{
	float a,b,c,d,total;

	cout<<"Numero a: ";cin>>a; 
	cout<<"Numero b: ";cin>>b;
	cout<<"Numero c: ";cin>>c;
	cout<<"Numero d: ";cin>>d;

	total = (a +b) / (c + d);

	cout.precision(3);
	cout<<"El total es: "<<total;
	return 0;
}