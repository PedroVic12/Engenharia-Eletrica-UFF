# Aula 15/09 - Funções

- Código limpo

<br>

## Variações nas listas de argumentos
###  Lista de Argumentos Variável
	- Pelo menos 1 argumento é obrigatório
	- `int func(int nArg1...) (<argumentos>);`

### Lista de argumentos Padrão
	- Na declaração da função, incorporar a inicialização por atribuição
	- `int func(int nArg1, int nArg2 =10, int nA3 =1) {<comandos>}`

##  **Passagem por referencia (importante)**
## Escopo em funções
	- São cradas na entrada da função e destruídas na Saida
	- Variáveis `Static` são globais para fins de armazenamentos mas locais quanto ao escopo.

## Sobrecarga de Funções
- Mecanismo que permite funções terem o mesmo identificador, desde que seus argumentos sejam diferentes (**tipo e quantidade**)

<br>

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
	

## Bibliotecas e Modulos

- Referencia de bibliotecas: 
`https://en.cppreference.com/w/cpp/header`

- É possível construir módulos com a inclusão de arquivos de cabeçalho, usando a extensão .h

- Os arquivos de cabeçalho tem os protótipos das funções 

- Para importar no código fonte, use

	`#include nome.h`	