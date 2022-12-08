#include <iostream>

using namespace std;

int *ponteiro1, *ponteiro2, vet[10];

// Atividade pratica: Alocação 


int main(int argc, char const *argv[])
{
    ponteiro1 = vet;
    ponteiro2 = &vet[0];

    if (ponteiro1 == ponteiro2){
        cout << "Endereços são iguais" << endl;
    }

    ponteiro1 = ponteiro1 + 5;

    cout << "\n";
    cout << vet[5] << endl;
    cout << *ponteiro1 << endl;


    return 0;
}
