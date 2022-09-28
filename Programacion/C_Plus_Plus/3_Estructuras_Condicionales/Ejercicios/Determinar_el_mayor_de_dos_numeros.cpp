#include<iostream>

using namespace std;

int main(int argc, char const *argv[])
{
	//Variables

	float num1,num2; 

	cout<<"Ingrese el primer numero: ";cin>>num1;
	cout<<"Ingrese el segundo número: ";cin>>num2;
	
	if (num1 == num2){
		cout<<"Los dos números son iguales";
	}else{
		if(num1 > num2){
			cout<<"El número "<<num1<<" es mayor";
		}else{
			cout<<"El número "<<num2<<" es mayor";
		}
	}

	return 0;
}