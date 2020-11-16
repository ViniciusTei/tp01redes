from core.Testes import Testes
from core.Estacao import Estacao


def main():

    maquinas = []  # lista de maquinas
    N = 20
    # menu
    # print("------------------------------\n")
    # print("   Escolha um valor para N:\n")
    # print("------------------------------\n")
    # N = int(input())  # numero de estacoes

    # inicializa lista de maquinas
    for i in range(N):
        m = Estacao(i, True, '000000001', 1)
        maquinas.append(m)

    #Testes.Aloha(maquinas, N)
    Testes.CSMA1P(maquinas, N)
    # print("------------------------------\n")
    # print("Voce escolheu", N, "estacoes\n")
    # print("Escolha um algoritmo:\n")
    # print("1- Aloha\n")
    # print("2- CSMA p-persistente\n")
    # print("3- Backoff Exponencial Binario\n")
    # print("------------------------------\n")
    # algoritmo = int(input())

    # if (algoritmo == 1):
    #     Testes.Aloha(maquinas, N)
    # elif(algoritmo == 2):
    #     Testes.CSMA1P(maquinas, N)
    # elif(algoritmo == 3):
    #     Testes.Backoff(maquinas, N)


if __name__ == "__main__":
    main()
