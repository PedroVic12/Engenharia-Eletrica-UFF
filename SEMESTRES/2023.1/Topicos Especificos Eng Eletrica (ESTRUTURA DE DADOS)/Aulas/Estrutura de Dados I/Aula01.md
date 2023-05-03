# Conteudo - 02/05/23

- Conceito de estrutura de dados
- Exemplo de Insertion Sort
- Análise Assintótica
- Notação O
- Notações Padrão 
- Correção de Algoritimos

## Estrutura de dados
- *É uma forma de armazenar e organizar dados de modo a facilitar operações de acesso e modificação*
- A escolha da estrutura de dados adequada faz parte do processo de solução de problema computacional
- Algoritmos a serem levados em consideração: Arvores de Decisão, Métodos Numericos, Algoritimos aproximativos, algoritimos Randomizados

## Correção de Algoritimo

Usar exemplos de Algoritimos simples como impar ou par para cada exemplo em C++

- *Contra Exemplo:* Se não é possivel construir contra-exemplos para as justificativas de um algoritimo, o algoritimo esta correto

- *Contradição:* Se as justificativas do algoritimo em nenhum caso produz resultados contraditórios, o algoritimo esta correto

- *Contraposição:* Se as justificativas do algoritimo estão corretas, a negação delas tambem estarão corretas

- *Indução*: Se o algoritimo permanece correto para quando o tamanho cresce monotonicamente, o algoritimo esta correto

- *Invariancia de Loop*: O algoritimo esta correto se as afirmações sao verdadeiras {L0, L1 ... L(k)}

	- Inicialização (L0): Afirmações iniciais L0 são verdadeiras *antes do inicio do loop*
	- Manutenção (L1): Se L(j-1) é verdadeiro antes da interação J, então L(j) será verdadeiro apos a iteração de j
	- Conclusão: Afirmações finais L(k) são..

	### Exemplo de invariancia de loop ao insertion Sort
	
	Em C++, o algoritmo de insertion sort pode ser implementado da seguinte maneira:

c++
``
void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}
``

Aqui, o loop principal é o for que itera sobre os índices i da lista de elementos desordenados. A cada iteração desse loop, o elemento arr[i] é inserido na posição correta da sublista ordenada arr[0..i-1].

A invariância do loop pode ser expressa da seguinte forma:

No início da i-ésima iteração do loop, a sublista arr[0..i-1] está ordenada.
Durante a i-ésima iteração do loop, o elemento arr[i] é inserido na posição correta da sublista arr[0..i-1], deslocando os elementos maiores para a direita.
No final da i-ésima iteração do loop, a sublista arr[0..i] está ordenada.


### Análise de Algoritimos
- Consiste em prever (ou estimar) o custo computacional de um algoritimo em termos de armazenamento e tempo de execução

- Se a analise experimental consiste...(continua no slide)

- *Análise Assintótica* : Permite estimar o comportamento de um algoritmo sem a necessidade de implementa-lo



