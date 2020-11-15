from src.Testes import Testes
from src.Estacao import Estacao

def main():
    N = 20 # numero de estacoes
    maquinas = [] # lista de maquinas

    # inicializa lista de maquinas
    for i in range(N):
        m = Estacao(i, False, '000000001', 1)
        maquinas.append(m)
    
    #Testes.Aloha(maquinas, N)
    Testes.CSMA1P(maquinas, N)
    
        
if __name__ == "__main__":
    main()




