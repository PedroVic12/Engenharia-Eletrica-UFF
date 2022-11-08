#include <iostream>
#include <cmath>

namespace senoide
{
    double A, omega, pi, f(double);  
} 

double senoide::f(double t){

    return A*sin(omega*t*pi);
}

int main(int argc, char const *argv[])
{
    double t = asin(1.0);
    senoide::A=100;
    senoide::pi=acos(0.0)/3;
    senoide::omega=377;

    std::cout << "f("<<t<<") = " << senoide::f(t) << '\n';
    
    return 0;
}

