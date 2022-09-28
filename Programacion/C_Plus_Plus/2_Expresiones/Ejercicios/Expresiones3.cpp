#include<iostream>
using namespace std;

int main(int argc, char const *argv[])
{
	// Variables

	float a = 0,b=0,c=0,d=0,e=0,f=0,resultado=0;

	cout<<"Digite 6 numeros";

	cout<<"Numero 1: "; cin>>a;
	cout<<"Numero 2: "; cin>>b;
	cout<<"Numero 3: "; cin>>c;
	cout<<"Numero 4: "; cin>>d;
	cout<<"Numero 5: "; cin>>e;
	cout<<"Numero 6: "; cin>>f;

	resultado = (a + (b/c)) / (d + (e/f));

	cout<<"El resultado es: "<<resultado;
	return 0;
}