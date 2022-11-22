#include <iostream>

using namespace std;

class Empregado
{
public:
    string Nome;
    string Empresa;
    int Idade;

    void seApresente()
    {
        cout << "Nome - " << Nome << endl;
        cout << "Empresa - " << Empresa << endl;
        cout << "idade - " << Idade << endl;
        cout << " " << endl;
    };
};

int main()
{

    Empregado empregado;
    empregado.Nome = "Pedro Victor";
    empregado.Empresa = "UFF";
    empregado.Idade = 24;
    empregado.seApresente();

    Empregado empregado_2;
    empregado_2.Nome = "John";
    empregado.Empresa = "Amazon";
    empregado.Idade = 35;
    empregado_2.seApresente();
};
