#include <iostream>
using namespace std;
#include <cmath>

double sinCos(double x, double y){
    return sin(x) + cos(y);
}

int main(int argc, char const *argv[])
{
    
    double (*ponteiroFuncao)(double, double) = sinCos;

    return 0;
}
