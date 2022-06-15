#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import numpy
import matplotlib.pyplot as plot

#Escreva seu nome e numero USP
INFO = {11820771:"André Luis Cardoso"}

def estima_pi(Seed = None):

    random.seed(Seed)
    #random.random() gera um numero com distribuicao uniforme em (0,1)
    """
    Esta funcao deve retornar a sua estimativa para o valor de PI
    Escreva o seu codigo nas proximas linhas
    """
    
    #determine o número de pontos
    n_pontos = 10000000
    
    ponto_dentro = 0
    ratio_list = []
    
    #este loop gera um número entre 0 e 1 para cada coordenada do ponto
    #assim que o ponto é gerado, ocorre a verificação, através da condição if, se ele consta dentro da área do círculo
    for i in range(1,n_pontos+1):
        ponto = [random.random(), random.random()]
        if numpy.sqrt(ponto[0]**2 + ponto[1]**2) <= 1:
            ponto_dentro += 1
        
        else:
            None
        ratio_list += [4 * (ponto_dentro/i)]
        
    #calculando a proporção de pontos dentro do círculo
    ratio = (ponto_dentro/(n_pontos))
    
    #plotando a estimativa ao longo dos pontos
    plot.figure(num=0,dpi=120)
    plot.plot(list(range(0,n_pontos)),ratio_list)
    plot.yticks(numpy.arange(min(ratio_list), max(ratio_list), 0.1))
    plot.axhline(y=4*ratio, color='r', linestyle='--')
     
    #retornaremos a área total do quadrado vezes a proporção que obtivemos
    return round(4 * ratio,5)


def media_estimativas(n):
    
    lista_estimativas = []
    for i in range(n):
        lista_estimativas += [estima_pi()]
        
    return round(numpy.mean(lista_estimativas),5)


def testando_erro():
     return (abs(3.14160-estima_pi()))/3.14164

        
        