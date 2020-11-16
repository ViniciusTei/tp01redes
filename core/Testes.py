import random
import math
from core.Estacao import Estacao


class Testes:
    def Aloha(maquinas, N):
        ativo = []  # maquinas que estao tentando enviar uma mensagem
        canaltempo = 0

        while(True):
            # verifica se eh o primeiro canal de tempo
            if(canaltempo == 0):
                canaltempo += 1
                # o canal esta ocupado, define True para sending de todas as maquinas
                for i in maquinas:
                    i.sending = True

                for m in maquinas:
                    if(m.sending):
                        ativo.append(m)
            else:
                canaltempo += 1
                # verifica colisoes
                if(len(ativo) > 1):
                    # recalcula o P
                    for m in ativo:
                        m.p = int((random.random()*10) + canaltempo)

                    # verifica quem vai tentar mandar msg novamente
                    for m in ativo:
                        # Caso P for igual ao canal de tempo vai tentar enviar a msg
                        if(m.p != canaltempo):
                            ativo.remove(m)

                elif(len(ativo) == 1):
                    for m in maquinas:
                        if(m.id == ativo[0].id):
                            m.sending = False
                            m.tempoGasto = canaltempo
                            print('Maquina: ', m.id)
                            print('Tempo gasto: ', m.tempoGasto * 51.2, 'us')

                    # reset dos ativos
                    ativo = []
                    for m in maquinas:
                        if(m.sending):
                            ativo.append(m)

                    # quando a lista de ativos ficar vazia nao existe mais nenhuma maquina tentando envair uma msg
                    if(len(ativo) == 0):
                        print('\nTempo total: ', canaltempo * 51.2, 'us')
                        break

    def CSMA1P(maquinas, N):
        ativo = []  # maquinas que estao tentando enviar uma mensagem
        esperandoNoCanal = []  # maquinas que querem transmitir em um determinado canal de tempo
        canaltempo = 0
        p = 1 # probabilidade de 1%
        canalOcupado = True
        # comeca a escutar os canais de tempo
        while(True):
            if(canaltempo == 0):
                canaltempo = 1
                for m in maquinas:
                    m.sending = True #Todas as maquinas querem enviar a partir do segundo canal de tempo
            else:
                for m in maquinas:
                    if (m.sending) and (m.p == canaltempo):  # maquina quer transmitir naquele canal
                        esperandoNoCanal.append(m)

                for m in esperandoNoCanal:  # verifica probabilidade da maquina transmitir
                    probabilidadeDeTransmitir = math.floor(random.random() * 100)  # valor entre 0 e 100
                    if(probabilidadeDeTransmitir <= p):
                        ativo.append(m)
                    else:
                        m.p += 1

                # Verificar as colisoes
                if(len(ativo) > 1):
                    # houve colisao tratar erro
                    for m in ativo:
                        m.p = math.floor((random.random()*100) + canaltempo)
                    
                    ativo.clear()

                elif(len(ativo) == 1):
                    # transmitir
                    flagEnd = 0
                    for m in maquinas:
                        if(m.id == ativo[0].id):
                            m.sending = False
                            m.tempoGasto = canaltempo
                            print('Maquina: ', m.id)
                            print('Tempo gasto: ', m.tempoGasto * 51.2, 'us')
                            ativo.clear()
                            break
                        elif(m.sending):
                            flagEnd += 1

                    if(flagEnd == 0):
                        print('\nTempo total: ', canaltempo * 51.2, 'us')
                        break

                canaltempo += 1

    def Backoff(maquinas, N):
        