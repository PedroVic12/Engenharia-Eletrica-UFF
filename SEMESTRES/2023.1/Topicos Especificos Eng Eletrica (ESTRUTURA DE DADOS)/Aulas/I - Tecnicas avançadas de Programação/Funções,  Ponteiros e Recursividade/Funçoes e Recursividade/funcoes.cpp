#include <array>
#include <iostream>

// Protótipo da função
int media(int, int, int);

//! Métodos

using namespace std;

void Escrever(string x)
{
    cout << "=========================" << '\n';
    cout << ">>>"
         << "Escrevendo na tela" << x << '\n';
    cout << "=========================" << '\n';
}

// Exemplo 1 - Cálculo de Média
int media(int x, int y, int z)
{
    int resultado = (x + y + z) / 3;
    return resultado;
}

// Exemplo 2 - Média Funcional
int media2(int x, int y, int z)
{
    int resultado = (x + y + z) / 3;
    return resultado;
}

int main()
{
    // Declaração de variáveis
    int a(5), b(6), c = 7, m;

    //Menu
    Escrever("Exemplo Média");

    // code
    m = media(a, b, c);
    std::cout << "Média 1 = " << m;

    return 0;
}
