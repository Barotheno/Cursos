#include<iostream>

using namespace std;

int main(int argc, char const *argv[])
{
	int numero;

	cout<<"Digita un número entre 1-5: ";cin>>numero;

	switch(numero){
		case 1: cout<<"Es el número 1"; break;
		case 2: cout<<"Es el número 2"; break;
		case 3: cout<<"Es el número 2"; break;
		case 4: cout<<"Es el número 4"; break;
		case 5: cout<<"Es el número 5"; break;
		default: cout<<"No esta en el grupo de rango de números"; break;
	}
	return 0;
}