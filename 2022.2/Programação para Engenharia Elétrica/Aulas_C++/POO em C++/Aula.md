# Conceitos de Programação Orientada a Objetos

## Abstração

- Extrair a essência de um objeto, características (atributos) e comportamentos (métodos) que o definem e que sejam do interesse do projeto. Exemplo: ma seccionadora tem varias características construtivas:

Cor movimentação ou tamanho. Para a sua automação, essas características não são consideradas.

- "Retirar do domínio do problema os detalhes relevantes e representa-los não mais na linguagem de domínio, e sim na linguagem da solução"

Montenegro, F (1994)

- **Domínio**: Conjunto de conceitos que definem o problema que sera resolvido pela programa

- Na POO, tem-se a **abstração de dados**,  onde uma estrutura de dados deve ser definida pelas operações que ocorrem com ela. Um objeto é um tipo de dado

## Objeto

- Uma entidade que exibe características e comportamentos. Na POO, é um construto de software que encapsula estado e comportamento, usando termos reais e abstrações (simplificações)

- Objetos interagem entre si através de mensagens

- Objetos são instancias de Classes

## Classe

- Define os atributos e comportamentos de um tipo de objeto

- **Atributos**: Características de uma classe que definem sua estrutura de dados

- **Comportamento**: Ação executada por um objeto. Pode ocorrer na passagem de uma mensagem ou na mudança de um estado. Também chamados de métodos

- **Construtores**: Métodos chamados na instanciação ou criação de um objeto da classe

- **Acessores**: Métodos que dão acesso aos dados internos de um objeto. Ex : getters

- **Mutantes**: Métodos que perimirem alterar o estado interno de um objeto. Ex: Setters

- Acesso aos membros (visibilidade): Publico (+), protegido(#), privado(-) ou pacote (*)

## Encapsulamento

- Característica de ocultar partes independentes da implementação

- O encapsulamento permite que alterações na implementação, que não alterem a interface, não tenham impacto na troca de mensagens com outros objetos

## Interface

- Lista os serviços oferecidos por um componente. Lista todos os métodos e argumentos que o objeto entende.

## Implementação

- Define como algo é feito. No caso da POO, é representada pelo código.

## Herança

- Classes podem ser criadas a partir de outras classes, possibilitando reuso de código da classe mãe.

## Associação  

- Uma classe fornece uma porção de código a outra, evitando a repetição de código

## Polimorfismo

- Propriedade de se usar o mesmo nome para métodos diferentes, implementados em diferentes níveis da hierarquia de classes
