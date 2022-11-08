#include <iostream>

using namespace std;

int operate(int a, int b)
{
	return (a * b);
};


float operate(float a, float b)
{
	return (a / b);
};

int main(int argc, char const *argv[])
{
	int x = 5, y = 10;

	float nX = 5.0, nY = 10.0;

	cout << "Resultado Inteiro: ";
	cout << operate(x, y);
	cout << "\n";
	cout << "\n";

	cout << "Resultado Float: ";
	cout << operate(nX, nY);
	cout << "\n";
	cout << "\n";

	return 0;
}
