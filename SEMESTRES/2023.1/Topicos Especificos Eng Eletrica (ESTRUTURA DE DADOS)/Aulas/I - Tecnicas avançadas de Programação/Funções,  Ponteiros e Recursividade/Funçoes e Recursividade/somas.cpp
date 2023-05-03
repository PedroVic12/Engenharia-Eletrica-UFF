#include <iostream>
double SomaValores(double a, double b) { return a + b; };
double SomaPonteiros(double *a, double *b) { return *a = *a + *b; };
double somar(double &, double &);
void Escrever(std::string x);

int main()
{
    double a = 5, b = 6, c = 7;
    std::string mensagem = "Exemplo Aula 18/04";
    Escrever(mensagem);
    std::cout << "Soma de valores: " << SomaValores(a, b) << '\n';
    std::cout << "Soma de ponteiros: " << SomaPonteiros(&a, &b) << '\n';
    std::cout << "Soma de referências: " << somar(a, b) << '\n';

    return 0;
}

// Passagem por referencia
double somar(double &a, double &b)
{
    return a += b;
}

using namespace std;

void Escrever(std::string x)
{
    std::cout << "=========================" << '\n';
    std::cout << ">>>"
              << "Escrevendo na tela " << x << '\n';
    std::cout << "=========================" << '\n';
}
