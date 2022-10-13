#include<iostream>
using namespace std;

int main(int argc, char const *argv[])
{
	char vocal;

	cout<<"Digite un caracter que sea una vocal: ";cin>>vocal;

	switch(vocal){
		case 'a':
		case 'e':
		case 'i':
		case 'o':
		case 'u': cout<<"Es una vocal minuscula";break;
		case 'A':
		case 'E':
		case 'I':
		case 'O':
		case 'U': cout<<"Es una vocal mayuscula";break;
		default : cout<<"No es una vocal";


	}
	return 0;
}