/*

	Realice un programa que lea de la entrada estándar los siguientes datos de una persona:

		Edad
		Sexo
		Altura

	Tras leer los datos, el programa debe mostrarlos en la salida estándar.
*/


#include<iostream>
using namespace std;

int main(int argc, char const *argv[])
{
	// Variables
	int edad;
	char sexo[10];//Especificamos cuantos carácteres
	float altura;
	// Cuestionario
	cout<<"\nHola y bienvenido por favor necesito la siguiente información";
	cout<<"\nCual es tu edad: ";cin>>edad;
	cout<<"\nEres Mujer u hombre: ";cin>>sexo;
	cout<<"\nPor ultimo, cuanto mides: ";cin>>altura;

	// Resultado

	cout<<"\nEstupendo, veamos ahora el resultado";
	cout<<"\nTu edad es de: "<<edad;
	cout<<"\nTu sexo es: "<<sexo;
	cout<<"\nTu altura es: "<<altura;

	return 0;
}