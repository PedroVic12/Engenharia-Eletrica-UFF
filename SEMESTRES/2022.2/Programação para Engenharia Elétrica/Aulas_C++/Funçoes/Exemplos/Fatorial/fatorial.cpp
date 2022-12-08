#include <iostream>

using namespace std;

int fatorial(int &z)
{
	int num_fatorial(1);
	for (int i = 0; i < z; i++)
	{
		num_fatorial = num_fatorial * i;
	};

	cout << "Valor de Z" << z << endl;
	return (num_fatorial);
}

int main()
{
	int numero, resultado;

	cout << "Entre com um numero inteiro: ";
	cin >> numero;
	resultado = fatorial(numero);
	cout << "Fatorial = " << resultado << "\n\n"
	     << endl;
	return 0;
}