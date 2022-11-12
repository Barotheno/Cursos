#include<iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    int x,y,elevacion;

    cout<<"Valor de x: ";cin>>x;
    cout<<"Valor de y: ";cin>>y;

    for ( i = 1; i <= y; i++)
    {
        elevacion = elevacion * x;
    }
    
    return 0;
}
