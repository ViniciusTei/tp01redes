import random

# classe que representa uma maquia/estacao
class Estacao:
    def __init__(self, id, sending, mesage, p):
        self.id = id
        self.sending = sending
        self.mesage = mesage
        self.p = p
        self.tempoGasto = 0

def main():
    N = 20 # numero de estacoes
    maquinas = [] # lista de maquinas
    ativo = [] # maquinas que estao tentando enviar uma mensagem 
    inativo = [] # maquinas que nao estao tentando enviar uma mensagem
    canaltempo = 0

    # inicializa lista de maquinas
    for i in range(N):
        m = Estacao(i, False, '000000001', 1)
        maquinas.append(m)

    while(True):
        # verifica se eh o primeiro canal de tempo
        if(canaltempo == 0):
            canaltempo+=1
            # o canal esta ocupado, define True para sending de todas as maquinas
            for i in maquinas:
                 i.sending = True
            
            for m in maquinas:
                if(m.sending):
                    ativo.append(m)
                else:
                    inativo.append(m)
        else:
            canaltempo+=1
            # verifica colisoes
            if(len(ativo) > 1):
                # recalcula o P
                for m in ativo:
                    m.p = int((random.random()*10) + canaltempo)

                #verifica quem vai tentar mandar msg novamente
                for m in ativo:
                    # Caso P for igual ao canal de tempo vai tentar enviar a msg
                    if(m.p != canaltempo):
                        ativo.remove(m)
                        inativo.append(m)

            elif(len(ativo) == 1):
                for m in maquinas:
                    if(m.id == ativo[0].id):
                        m.sending = False
                        m.tempoGasto = canaltempo
                        print('Maquina: ', m.id)
                        print('Tempo gasto: ', m.tempoGasto * 51.2, 'us')
                
                # reset dos ativos
                ativo = []
                inativo = []
                for m in maquinas:
                    if(m.sending):
                        ativo.append(m)
                    else:
                        inativo.append(m)

                # quando a lista de ativos ficar vazia nao existe mais nenhuma maquina tentando envair uma msg
                if(len(ativo) == 0):
                    print('\nTempo total: ', canaltempo  * 51.2, 'us')
                    break
        
main()




