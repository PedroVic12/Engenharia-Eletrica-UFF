
## Dividir para conquistar(...)

- Dividir o problema em um numero de subproblemas que sao instancias menores do mesmo problema

- Conquistar os subproblemas resolvendo os rercusivamente

- Combinar as soluções dos subproblemas

### Tipos
- Caso recursivo: Quando o subproblema é suficiente grande para ser resolvido recursivamente

- Caso Base: Quando o subproblema é pequeno ao ponto de não ser necessário a recursão.

### Exemplo: Algoritimo Merge Sort em python

```
# Função que mescla duas listas ordenadas em uma única lista ordenada
def merge(lista1, lista2):
    resultado = []  
    i = 0  # Variável de índice para a lista1
    j = 0  # Variável de índice para a lista2
    
    # Loop para mesclar as duas listas enquanto houver elementos iguais em ambas
    while i < len(lista1) and j < len(lista2):
        if lista1[i] <= lista2[j]: 
            resultado.append(lista1[i]) 
            i += 1  # Move o índice para a próxima posição da lista1
        else:  
            resultado.append(lista2[j])  
            j += 1  # Move o índice para a próxima posição da lista2
    
    # Adiciona o restante dos elementos da lista1 e/ou lista2, caso ainda existam
    resultado += lista1[i:]
    resultado += lista2[j:]
    
     # Retorna a lista mesclada em ordem crescente
    return resultado 


def merge_sort(lista):

    # Caso base: a lista contém 0 ou 1 elementos e já está ordenada
    if len(lista) <= 1:
        return lista

    # Divide a lista em duas partes
    meio = len(lista) // 2 
    lista_esquerda = lista[:meio]  # Lista com os elementos da primeira metade
    lista_direita = lista[meio:]  # Lista com os elementos da segunda metade
    
    # Chamada recursiva da função merge_sort para ordenar cada metade da lista
    lista_esquerda = merge_sort(lista_esquerda)
    lista_direita = merge_sort(lista_direita)
    
    # Chama a função merge para mesclar as duas metades da lista em uma lista ordenada
    return merge(lista_esquerda, lista_direita)



``
