#include<iostream>
using namespace std;

int main(int argc, char const *argv[])
{
	int n1,n2,n3,n4;

	cout<<"\n\t[*] Comprobaremos si tu numero concide con los 3 primeros que introduces [*]\n";

	cout<<"Digite el primer numero: ";cin>>n1;
	cout<<"Digite el segudo numero: ";cin>>n2;
	cout<<"Digite el tercer numero: ";cin>>n3;

	cout<<"\n\t@@ A continuacion veamos los números que introduciste:";
	cout<<"\n\tNumeros: "<<n1+" | "<<n2+" | "<<n3;

	cout<<"\nAhora digite el cuarto numero: \n";cin>>n4;

	if (n4 == n1)
	{
		cout<<"Su numero es igual a: "<<n1;
	}else if (n4 == n2){
		cout<<"Su numero es igual a: "<<n2;
	}else if (n4 == n3){
		cout<<"Su numero es igual a: "<<n3;
	}else{
		cout<<"Es diferente a los tres anteriores";
	}

	return 0;
}