/*
	Escribir un programa que de la entrada estándar el precio de de un producto y muestre en la salida estándar el
	precio del producto al aplicarle el IVA
*/
#include<iostream>

using namespace std;

int main(int argc, char const *argv[])
{
	float precio = 0, iva = 0, precio_iva = 0, total = 0;

	cout<<"Hola! Tienes problemas para calcular el iva... Hummm que mal rollo!!!\n";
	cout<<"Bueno bueno no te preocupes yo estoy aqui para ayudarte.\n"; 
	cout<<"\nVenga dime el precio y yo te sumo el iva: ";cin>>precio; 
	cout<<"\nYeahhhh baby ahora dime de cuanto IVA estamos hablando: ";cin>>iva;


	precio_iva = (precio * iva) / 100;
	total = precio_iva + precio;

	cout<<"El IVA seria el siguiente: "<<precio_iva;
	cout<<"\nAmigo mio, me temo que te toca pagar un total de: "<<total;
	return 0;
}