// Se ejecutarán el conunto de acciones al menos una ved

#include<iostream>
// La libreria stdlib.h tiene una funcion especial que es el system pause.
// Lo que hace esque no permite avanzar en el programa hasta que no presionemos una tecla
#include<stdlib.h>


using namespace std;

int main(int argc, char const *argv[])
{
	int i;

	i = 1;

	do{
		cout<<i<<end1;
		i++;
	}while(i<=10);

	system("pause");

	return 0;
}