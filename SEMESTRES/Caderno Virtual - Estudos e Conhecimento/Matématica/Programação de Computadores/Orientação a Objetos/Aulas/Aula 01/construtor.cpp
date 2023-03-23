#include <iostream>

using namespace std;

class Empresa:
{
public:
    string Name;
    string Company;
    int Age;

    void seApresente()
    {
        cout << "Nome - " << Name << endl;
        cout << "Empresa - " << Company << endl;
        cout << "idade - " << Age << endl;
        cout << " " << endl;
    };


    funcionario(string nome, string nome_empresa, int idade){
        Name = nome;
        Company = nome_empresa;
        Age = idade;
    };
    
};

int main()
{

    Empresa funcionario_1 = Empresa("Pedro","UFF",24);
    funcionario_1.seApresente();

    Empresa funcionario_2 = Empresa("John","Google", 35);
    funcionario_2.seApresente();
};
