#include <iostream>
using namespace std;
struct estrutura3
{
    int chave;
    estrutura3 *proximo;
};

void print(estrutura3 *root)
{

    estrutura3 *numero = root;

    // loop
    while (numero->proximo != nullptr)
    {
        cout << 'Continue :' << endl;
    }
}
