#include <iostream>
using namespace std;

class Ccomplex
{

    // Letra B) Atributos
private:
    double _real, _img;

public:
    // Letra C) Construtores
    Ccomplex()
    {
        this->_img = 0;
        this->_real = 0;
    };

    Ccomplex(double real)
    {
        this->_img = 0;
        this->_real = real;
    };

    Ccomplex(double real, double img)
    {
        this->_img = img;
        this->_real = real;
    };

    // Letra D) Destruidor
    ~Ccomplex()
    {
        cout << "Destruidor" << endl;
    }

    // Letra E) Métodos
    void print()
    {
        cout << "[ " << _real << " " << _img << "J "
             << "]" << endl;
    }

    // Letra F) Getters
    double get_real()
    {
        return _real;
    };

    double get_imaginario()
    {
        return _img;
    };

    // Letra G) Métodos
    void somar(){

    };

    void subtrair(){

    };

    void multiplicar(){

    };

    void dividir(){

    };
};

int main()
{
    Ccomplex numero_complexo1;

    return 0;
}