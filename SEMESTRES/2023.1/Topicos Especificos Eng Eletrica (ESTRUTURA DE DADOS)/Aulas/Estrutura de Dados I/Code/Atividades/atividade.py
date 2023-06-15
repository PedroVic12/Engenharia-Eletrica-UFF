class No:
    def __init__(self, chave):
        self.chave = chave
        self.prox = None


class ListaEncadeada:
    def __init__(self):
        self.head = None
        self.tail = None
        self.tam = 0

    def adicionar_no(self, chave):
        novo_no = No(chave)

        #Checa ao head se esta vazio
        if self.head is None:
            self.head = novo_no
        else:
            self.tail.prox = novo_no

        #Adiciona o no e aumenta a lista
        self.tail = novo_no
        self.tam += 1

    def imprimir_lista(self):
        no_atual = self.head
        while no_atual is not None:
            print(no_atual.chave)
            no_atual = no_atual.prox

    def intercalar(self, lista1, lista2):
        lista_C = ListaEncadeada()

        # Inicializando o no em cada head da lista
        no_lista1 = lista1.head
        no_lista2 = lista2.head

        #loop para checar os valores de cada lista
        while no_lista1 is not None and no_lista2 is not None:
            lista_C.adicionar_no(no_lista1.chave)
            lista_C.adicionar_no(no_lista2.chave)

            no_lista1 = no_lista1.prox
            no_lista2 = no_lista2.prox

        while no_lista1 is not None:
            lista_C.adicionar_no(no_lista1.chave)
            no_lista1 = no_lista1.prox

        while no_lista2 is not None:
            lista_C.adicionar_no(no_lista2.chave)
            no_lista2 = no_lista2.prox

        return lista_C
        while no_lista1 is not None:
            lista_C.adicionar_no(no_lista1.chave)
            no_lista1 = no_lista1.prox


# Exemplo de uso da lista encadeada
lista_A = ListaEncadeada()
lista_A.adicionar_no("w")
lista_A.adicionar_no("x")
lista_A.adicionar_no("y")
lista_A.adicionar_no("z")
lista_A.imprimir_lista()
print("\n")

# Exemplo B
lista_B = ListaEncadeada()
lista_B.adicionar_no("R")
lista_B.adicionar_no("S")
lista_B.imprimir_lista()
print("\n")

# Exemplo C
lista_C = ListaEncadeada()
lista_C = lista_C.intercalar(lista_A, lista_B)
lista_C.imprimir_lista()
