#include <iostream>
using namespace std;

class CRectangle {
    int x, y;

    public:
        // método setter(boa pratica) apenas declaração 
        void set_values(int,int);

        //método área
        int area(){
            return x*y;
        }

};

//Parecido com o self.set_values (pode ser feita dentro da classe acima)
void CRectangle::set_values (int a, int b){
    x = a;
    y = b;
}

int main(){
    CRectangle retangulo;
    retangulo.set_values(3,4);
    cout << "Área do retangulo = " << retangulo.area() << " Metros quadrados";
    return 0;
}