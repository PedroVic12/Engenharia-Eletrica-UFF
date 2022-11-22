#include <iostream>
using namespace std;

class A
{
protected:
    int v;

public:
    A()
    {
        v = 1;
    };

    ~A(){};

    void m1()
    {
        v = v + 10;
        m2();
    };

    void m2()
    {
        v = v + 20;
    };

    int get_v()
    {
        return v;
    };
};

class B : public A
{
public:
    void m2()
    {
        v = v + 30;
    };
};

/*
Letra A) Se essas classes forem utilizadas a partir do programa a seguir, o que será
impresso na tela ao executarmos o código?

     OUTPUT = 61

*/

/*
Letra B) Quando o código Obj -> m2() é executado no programa
o que acontece com o valor no atributo v?

     // OUTPUT = 61


*/

int main()
{
    // Instanciando a Classe com ponteiro
    B *Obj = new B();
    // OUTPUT: V = 1

    // Invocando os métodos
    Obj->m1();
    // OUTPUT: V = 31

    Obj->m2();
    // OUTPUT = 61

    cout << Obj->get_v() << endl;

    return 0;
}

/*
Letra C)

Sim, A *Obj = new A();

A diferença é o OUTPUT = 51
*/

/*
Letra D)

Não, pois não é possível acessar a variável v dentro do o método m2() dentro a classe B
*/