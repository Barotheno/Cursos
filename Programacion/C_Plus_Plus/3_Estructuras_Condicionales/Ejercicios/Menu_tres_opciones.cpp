#include<iostream>
#include<math.h>

using namespace std;

int main(int argc, char const *argv[])
{
    int opcion;
    float numero;
    int numero2;
    float cubo;

    cout<<"\t.:MENU:.\n";
    cout<<"1. Cubo de un numero\n";
    cout<<"2. Numero par o inpar\n";
    cout<<"3. Salir\n";
    cout<<"Opcion: ";
    cin>>opcion;

    switch (opcion)
    {
    case 1: cout<<"\nDigite un numero: ";cin>>numero;
            cubo = pow(numero,3);
            cout<<"\nEl resultado es: "<<cubo;
            break;
    case 2: cout<<"\nDigite un numero: ";cin>>numero2;
            if ((numero2 % 2) == 0)
            {
                cout<<"\nEl numero es par";
            }else
            {
                cout<<"\nEs impar";
            }
            break;
    case 3: cout<<"\nUsted a elegido salir, esperemos bolverle a ver pronto.";
            break;
            
            
    }

    return 0;
}
