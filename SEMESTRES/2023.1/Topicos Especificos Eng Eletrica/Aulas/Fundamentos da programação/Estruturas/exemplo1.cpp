#include <iostream>
using namespace std;

//! Listas encadeadas é 

struct estrutura
{
    int chave;
    estrutura *proximo; // apontador
};

int main(int argc, char const *argv[])
{
    int ponteiroVazio;
    estrutura head = {1, nullptr};
    estrutura no1 = {2, nullptr};

    head.proximo = &no1;
    cout << 'Chave Head :' << head.chave << endl;
    cout << 'Proximo head: ' << head.proximo << endl;

    cout << 'Chave No1: ' << no1.chave << endl;
    cout << 'Ponteiro No1' << head.proximo->chave << endl;

    // cout << 'Proximo estrutura: ' << estrutura.proximo << endl;

    // atribuindo
    estrutura *ponteiro = &head;

    return 0;
}
