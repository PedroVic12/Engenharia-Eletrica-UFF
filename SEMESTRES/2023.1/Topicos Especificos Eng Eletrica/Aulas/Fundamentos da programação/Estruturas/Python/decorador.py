import time


def decorater(funcao):
    def wrapper(inicio, fim):

        print("Iniciando a função")
        funcao(inicio, fim)
        tempo_inicio = time.time()
        contagem = funcao(inicio, fim)
        dt = time.time() - tempo_inicio
        print("Finalizando a função")
        print("Tempo de execução: %0.8f segundos." % dt)

    return wrapper


@decorater
def contagem(inicio=0, fim=1000):
    for i in range(1, 5):
        print(i)
        contador = i

        time.sleep(1)
        return contador


contagem(0, 10)
