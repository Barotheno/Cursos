#include<iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    int numero = 0;
    int multiplicador = 10;

    cout<<"\t\t\n[*] BIENVENIDO AL MULTIPLICADOR [*]";

    do{
    cout<<"\t\nPor favor, digite el numero que quiere multiplicar: ";cin>>numero;
    }while((numero<1) || (numero>1000));

    for(int i=1;i<=10;i++){
        int resultado = i * numero;
        cout<<numero<<" * "<<i<<" = "<<resultado<<endl;
    }

    return 0;
}
