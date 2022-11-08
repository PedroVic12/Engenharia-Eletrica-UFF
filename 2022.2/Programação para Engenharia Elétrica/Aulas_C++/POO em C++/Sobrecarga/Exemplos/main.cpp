// Sobrecarga de Operadores
#include <iostream>

class CVector
{
private:
    float x, y;

public:
    // sobrecarga no construtor
    CVector()
    {
        x = 1.0, y = 1.0;
    }

    CVector(float fx, float fy)
    {
        x = fx;
        y = fy;
    }

    // Sobrecarga no operador binário + para somar dois objetos Vector
    CVector operator+(const CVector v)
    {
        CVector temp;
        //this é um ponteiro (precisa do ->)
        temp.x = this->x + v.x;
        temp.y = this->y + v.y;
        return temp;
    }

    // Sobrecarga no operador unário ++ prefixado para incrementar objetos Vector
    CVector operator++()
    {
        x = x + 1;
        y = y + 1;
        return CVector(x, y);
    }

    void print()
    {
        std::cout << "x = " << this->x << "\t y = " << this->y << std::endl;
    }
};

int main(){
    CVector vetor_t, vetor_inc, vetor1, vetor2;

    //soma dois valores unitários
    vetor_t = vetor1 + vetor2;

    //resultado
    vetor_t.print();

    //incrementa vetor resultante
    vetor_inc = vetor_t.operator++();

    //imprime no novo resultado
    vetor_t.print();
    vetor_inc.print();

    return 0;
};