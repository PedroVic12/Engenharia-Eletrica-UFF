#include <iostream>
using namespace std;

class Base
{
    int m_x;

public:
    Base(int x)
    {
        int y = 100, x = 100;
        this->m_x = y * x;
        cout << "Base() \n";
    };

    ~Base()
    {
        cout << "~Base() \n";
    }

    void print()
    {
        cout << " Base: " << m_x << "\n";
    }

    virtual int utopia(int, int) = 0;

    friend void universe(float);
};

class Derived : public Base
{
    int m;

public:
    Derived(int y) : Base(y)
    {
        cout << "Derived() \n";
    };

    ~Derived()
    {
        cout << "~Derived() \n";
    }

    void print()
    {
        cout << " Derived: " << m_x << "\n";
        // m_x esta inaccessível e não consegue herdar da classe Base
    }

    virtual int utopia(int ideias, int pessoas)
    {
        if ((ideias > 1) && (pessoas > 2))
        {
            return (0);
        }
        else
        {
            return (1);
        };
    };

    void universe(float matter)
    {
        float zero = 0.00001;
        Derived higgs(0);
        matter = zero * higgs.m;
        cout << "Matter = " << matter << endl;
    }
};

int main()
{
    Derived d(5), e(4);
    Base b1(10);
    // Objeto do Tipo Base não é permitido

    Base *b = &0;

    int ragnarok, tao;
    ragnarok = b->utopia(1, 1);
    tao = b1.utopia(0, 0);

    cout << "Ragnarok"
         << " \t" << tao << "\n";
    d.universe(10.0);
    d.print();
    b.print();
    // A expressão precisa ser do tipo de Classe Base mas é um ponteiro
};