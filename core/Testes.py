import random
import math
import statistics
from core.Estacao import Estacao
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


class Testes:
    def Aloha(maquinas, N):
        ativo = []  # maquinas que estao tentando enviar uma mensagem
        canaltempo = 0
        tempoPrimeiraMaquina = 0
        first = True #
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
                            if(first):
                                #print('Maquina: ', m.id)
                                #print('Tempo gasto: ', m.tempoGasto * 51.2, 'us')
                                tempoPrimeiraMaquina =  m.tempoGasto
                                first=False

                    # reset dos ativos
                    ativo = []
                    for m in maquinas:
                        if(m.sending):
                            ativo.append(m)

                    # quando a lista de ativos ficar vazia nao existe mais nenhuma maquina tentando envair uma msg
                    if(len(ativo) == 0):
                        #print('\nTempo total: ', canaltempo * 51.2, 'us')
                        
                        break
        return tempoPrimeiraMaquina, canaltempo
    
    def CSMA1P(maquinas, N):
        ativo = []  # maquinas que estao tentando enviar uma mensagem
        esperandoNoCanal = []  # maquinas que querem transmitir em um determinado canal de tempo
        canaltempo = 0
        p = 1 # probabilidade de 1%
        first = True #primeira estacao a transmitir
        tempoPrimeiraMaquina = 0

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

                canaltempo += 1
                # Verificar as colisoes
                if(len(ativo) > 1):
                    # houve colisao tratar erro
                    for m in ativo:
                        m.p = math.floor((random.random()*100)) + canaltempo
                    
                    #ativo.clear()

                elif(len(ativo) == 1):
                    # transmitir
                    for m in ativo:
                        m.sending = False
                        m.tempoGasto = canaltempo
                        if(first):
                            tempoPrimeiraMaquina = m.tempoGasto
                            first = False
                        #print('Maquina: ', m.id)
                        #print('Tempo gasto: ', m.tempoGasto, 'us')
                
                ativo.clear() #sempre limpa a lista de ativos
                esperandoNoCanal.clear() #sempre limpa a lista das maquinas esperando naquele canal
                flagEnd = 0
                for m in maquinas:
                    if(m.sending):
                        flagEnd +=1

                if(flagEnd == 0):
                    #print('\nTempo total: ', canaltempo, 'us')
                    break
        return tempoPrimeiraMaquina, canaltempo
    
    def Backoff(maquinas, N):
        ativo = []  # maquinas que estao tentando enviar uma mensagem
        canaltempo = 0
        first = True #primeira estacao a transmitir
        tempoPrimeiraMaquina = 0
        # comeca a escutar os canais de tempo
        while(True):
            if(canaltempo == 0):
                canaltempo = 1
                for m in maquinas:
                    m.sending = True #Todas as maquinas querem enviar a partir do segundo canal de tempo
            else:
                #canal livre maquinas querem enviar
                for m in maquinas:
                    if(m.sending) and (m.p == canaltempo):
                        ativo.append(m)
                
                canaltempo += 1
                #tratar colisoes
                if(len(ativo) > 1):
                    for m in ativo:
                        m.backoff_value +=1 # aumenta o valor de backoff
                        if(m.backoff_value < 10): # quando backoff eh menor q 10 usa o valor dele, se nao eh sempre 10
                            m.p = (random.randrange(0, (2 ** m.backoff_value ))) + canaltempo # escolhe um novo slot entre 0 e (2^c - 1)
                        else:
                            m.p = (random.randrange(0, (2 ** 10))) + canaltempo
                    ativo.clear()
                
                elif(len(ativo) == 1): # envia mensagem
                    for m in ativo:
                        m.sending = False
                        m.tempoGasto = canaltempo
                        if(first):
                            tempoPrimeiraMaquina = m.tempoGasto
                            first = False
                        #print('Maquina: ', m.id)
                        #print('Tempo gasto: ', m.tempoGasto * 51.2, 'us')
                        break
                    
                    ativo.clear()
                
                flagEnd = 0
                coutSending = 0
                for m in maquinas:
                    if(m.backoff_value >= 16):
                        flagEnd = 1
                    elif(m.sending):
                        coutSending += 1
                
                if(coutSending == 0) or (flagEnd == 1):
                    #print('\nTempo total: ', canaltempo * 51.2, 'us')
                    break
                
        return tempoPrimeiraMaquina,canaltempo

    def calculaResultado(tempo, algoritmo, n):
        tempo_primeira = []
        tempo_total = []

        #desestruturacao da tupla para facilitar o calculo das medias
        for t in range(len(tempo)):
            tempo_primeira.append(tempo[t][0])
            tempo_total.append(tempo[t][1])

        media_primeira = statistics.mean(tempo_primeira)
        media_total = statistics.mean(tempo_total)
        desvio_pirmeiro = statistics.pstdev(tempo_primeira, media_primeira)
        desvio_total = statistics.pstdev(tempo_total, media_total)
        print("------- Resultado ---------")
        print("Algoritmo: ", algoritmo)
        print("Valor de N: ", n)
        print("Media primeira estacao: ", media_primeira, " Desvio: ", desvio_pirmeiro)
        print("Media total: ", media_total, " Desvio: ", desvio_total)
        print("--------------------------------")

    def executaTestes(N):
        tempo = []
        maquinas = []  # lista de maquinas
        
        for i in range(0,33):
            # inicializa lista de maquinas
            for j in range(N):
                m = Estacao(j, False, '000000001', 1)
                maquinas.append(m)
            tempo.append(Testes.Aloha(maquinas, N))
            maquinas.clear()

        Testes.calculaResultado(tempo, 'Aloha', N)
        tempo.clear()

        for i in range(0,33):
            # inicializa lista de maquinas
            for j in range(N):
                m = Estacao(j, False, '000000001', 1)
                maquinas.append(m)
            
            tempo.append(Testes.CSMA1P(maquinas, N))
            maquinas.clear()
        
        Testes.calculaResultado(tempo, 'CSMA-P', N)
        tempo.clear()

        for i in range(0,33):      
            # inicializa lista de maquinas
            for j in range(N):
                m = Estacao(j, False, '000000001', 1)
                maquinas.append(m)          
            
            tempo.append(Testes.Backoff(maquinas, N))
            maquinas.clear()

        Testes.calculaResultado(tempo, 'Backoff', N)
        tempo.clear()
