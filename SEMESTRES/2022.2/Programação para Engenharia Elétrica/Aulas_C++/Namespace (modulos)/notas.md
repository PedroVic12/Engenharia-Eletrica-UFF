# Namespace ou Módulos

- Definição: Decomposição de um programa em partes
- Encapsulamento dos dados: Se um objeto nao utiliza um dado, não deve
ter acesso a ela
- Legibilidade de um programa, evita múltiplas declarações, redefinições e etc

- C++ não possui módulos

## O que é Namespaces?
- Escopo para um conjunto de objetos
- Os membros do namespace estão no mesmo escopo, sendo visíveis entre si
- Para que os membros seja, visíveis fora do namespace, deve-se utilizar
um nome qualificado para alcançar o escopo

- Um namespace representa uma unidade lógica de um programa

- Deve conter apenas objetos associados a uma tarefa específica

## Usando o Using
- O uso de nomes qualificados pode ser tedioso ou deixar o código muito poluído
- Declarações e diretivas using permitem suprimir a qualificação, tornando o código mais limpo
- Declaração using para um objeto namespace

## Diretivas de pré-processamento
- Iniciam com # e não finalizam com ;
- Inclusão de arquivos de cabeçalho (#include)
- #define 

## Modularização
- Arquivo de interfaces, protótipos se usa a extensão .h
- Arquivo principal e namespace se usa a extensão .cpp