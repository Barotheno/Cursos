#include<iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    int suma = 0, cuadrado;

    for( int i=1; i<=10;i++){
        cuadrado = i * i;
        suma = suma + cuadrado;
        cout<<"\nEl resultado de la suma es: "<<suma;
    }
    cout<<"\nEl resultado de la suma es: "<<suma;
    return 0;
}
