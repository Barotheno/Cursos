#include<iostream>
//Necesitamos la libreria math.h para realizar raices cuadradas
// "sqrt(): Raiz Cuadrada"
// "pow(): "Elevar a la potencia deseada"
#include<math.h>
using namespace std;

int main(int argc, char const *argv[])
{
	// Variables

	float hipotenusa,catetoB,catetoC;

	cout<<"Introduce el primer cateto: ";cin>>catetoB;
	cout<<"Introduce el segundo cateto: ";cin>>catetoC;

	hipotenusa = sqrt(pow(catetoB,2)+pow(catetoC,2));

	cout.precision(2);
	cout<<"La hipotenunca del triangulo rectangulo es: "<<hipotenusa;
	return 0;
}