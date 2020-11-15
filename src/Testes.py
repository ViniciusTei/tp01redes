import random
from src.Estacao import Estacao

class Testes:    
    def Aloha():
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

    def CSMA1P():
        N = 20 # numero de estacoes
        maquinas = [] # lista de maquinas
        ativo = [] # maquinas que estao tentando enviar uma mensagem 
        esperandoNoCanal = [] # maquinas que querem transmitir em um determinado canal de tempo
        canaltempo = 0
        p = 0.01

        # inicializa lista de maquinas
        for i in range(N):
            m = Estacao(i, False, '000000001', 1)
            maquinas.append(m)

        #comeca a escutar os canais de tmepo
        while(True):
            #primeiro canal de tempo
            if(canaltempo == 0):
                canaltempo = 1 # nada acontece
            else:
                for m in maquinas:
                    if(m.p == canaltempo): #maquina quer transmitir naquele canal
                        esperandoNoCanal.append(m)
                
                for m in esperandoNoCanal: #verifica probabilidade da maquina transmitir
                    probabilidadeDeTransmitir = (random.random() / 10) # valor entre 0 e 0.1
                    if(probabilidadeDeTransmitir == p):
                        ativo.append(m)
                    elif(probabilidadeDeTransmitir == (1-p)):
                        m.p+=1
                
                #Verificar as colisose
                if(len(ativo) > 1):
                    #houve colisao tratar erro
                    for m in ativo:
                        m.p = int((random.random()*10) + canaltempo)

                elif(len(ativo) == 1):
                    #transmitir
                    flagEnd = 0
                    for m in maquinas:
                        if(m.id == ativo[0].id):
                            m.sending = False
                            m.tempoGasto = canaltempo
                            print('Maquina: ', m.id)
                            print('Tempo gasto: ', m.tempoGasto * 51.2, 'us')
                            ativo.clear()
                        elif(m.sending):
                            flagEnd+=1
                    
                    if(flagEnd == 0):
                        print('\nTempo total: ', canaltempo  * 51.2, 'us')
                        break

            canaltempo+=1
                
                
                    

                


