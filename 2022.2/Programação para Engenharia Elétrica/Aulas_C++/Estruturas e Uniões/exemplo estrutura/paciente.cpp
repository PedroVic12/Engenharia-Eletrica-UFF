#include <iostream>

using namespace std;

struct paciente
{
    //Estruturas
    int idade;
    float peso, altura;

 // Objetos (pessoas)   
}João,Pedro, Maria;


struct Unidade_Hospital
{
    int leitos, day_in,day_out;
    paciente internados[20];
}UPA;



int main(int argc, char const *argv[])
{
    int lista[5];
    paciente joão, pedro;
    pedro.idade = 24;
    pedro.peso = 70.5;

    UPA.internados[0].peso = 71.0;

    cout << UPA.internados[0].peso<< endl;
    

    return 0;
}

int main_ponteiros(int argc, char const *argv[])
{
    paciente pedro, *maria;
    pedro.idade = 30;

    //Inicialização do ponteiro maria
    maria = new paciente;

    //Equivale a (*maria).idade = 40
    maria -> idade = 40;
    maria -> peso = 60.5;




    return 0;
}

