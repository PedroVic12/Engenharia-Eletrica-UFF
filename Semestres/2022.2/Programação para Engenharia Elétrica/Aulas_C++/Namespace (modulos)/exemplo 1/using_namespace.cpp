#include <iostream>
#include <cmath>

namespace senoide
{
    double A, omega, pi, f(double);  
} 

double senoide::f(double t){

    return A*sin(omega*t*pi);
}

//Utilizando o Using
using namespace senoide;

int main(int argc, char const *argv[])
{
    using std::cout;
    double t = asin(1.0);
    A=100;
    pi=acos(0.0)/3;
    omega=377;

    cout << "f("<<t<<") = " << senoide::f(t) << '\n';

    return 0;
}

