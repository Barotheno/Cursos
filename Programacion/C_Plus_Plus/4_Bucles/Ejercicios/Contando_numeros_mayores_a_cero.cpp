#include<iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    int numero,conteo = 0;

    do
    {
        cout<<"Digite numeros: ";cin>>numero;
        if(numero>0){
            conteo++;
        }
    } while (numero != 0);

    cout<<"El numero de valores mayores a cero introducidos es: "<<conteo;
    
   
    return 0;
}
