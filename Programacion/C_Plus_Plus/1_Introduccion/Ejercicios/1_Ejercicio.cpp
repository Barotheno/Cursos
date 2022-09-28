/*
	1

	Escribe un programa que lea de la entrada estándar dos números muestre en la salida estándar su suma, resta, multiplicación y 
	división.
*/


#include<iostream>

using namespace std;

int main(int argc, char const *argv[])
{
	int num1 = 0;
	int num2 = 0;
	float suma = 0, resta = 0, mult = 0, div = 0;

	cout<<"\nDigite el primer número: ";cin>>num1;
	cout<<"\nDigite un segundo número: ";cin>>num2;

	suma = num1 + num2;
	resta = num1 - num2;
	mult = num1 * num2;
	div = num1 / num2;

	cout<<"\nEl valor de la suma es: "<<suma;
	cout<<"\nEl valor de la resta es: "<<resta;
	cout<<"\nEl valor de la multiplicación es: "<<mult;
	cout<<"\nEl valor de la división es: "<<div; 


	return 0;
}