#include<iostream>
using namespace std;

int main(int argc, char const *argv[])
{
	float n1;

	cout<<"Digite un número: ";cin>>n1;

	if (n1 == 0)
	{
		cout<<"El número es cero";
	}else if (n1 > 0){
		cout<<"El número es positivo";
	}else{
		cout<<"El número es negativo";
	}

	return 0;
}