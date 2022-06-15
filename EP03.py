#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
from scipy.stats import qmc

#Escreva seu nome e numero USP
INFO = {11820771:"André Luis Cardoso"}
A = 0.262143264  # A = 0.rg
B = 0.91936739062  # B = 0.cpf



def f(x):
    """
    Esta funcao deve receber x e devolver f(x), como especifcado no enunciado
    Escreva o seu codigo nas proximas linhas
    """
    
    return np.exp(-A*x)*np.cos(B*x)

def g(x):
    """
    Variável de Controle
    
    """
    return -0.6*x + 1.05



def crude(n = 300000, Seed = None):
    random.seed(Seed)
    """
    Esta funcao deve retornar a sua estimativa para o valor da integral de f(x)
    usando o metodo crude
    Escreva o seu codigo nas proximas linhas
    """
    
    soma = 0
    lista_estimativas = []
    N = n
    
    points = qmc.Sobol(d=1, scramble=True)
    qrpoints = points.random_base2(m=int(np.around(np.log2(n))))
    
    
    #gerando pontos uniformemente e aplicando na função
    n=1
    for i in qrpoints:
        soma += f(i)
        lista_estimativas += [soma/n]
        n+=1
        
    """
    plt.figure(num=0,dpi=120)    
    plt.plot(list(range(len(lista_estimativas))),lista_estimativas)
    plt.yticks(np.arange(min(lista_estimativas), max(lista_estimativas), 0.1))
    """    
    
    return float(lista_estimativas[-1])





def hit_or_miss(n = 3000000, Seed = None):
    random.seed(Seed)
    """
    Esta funcao deve retornar a sua estimativa para o valor da integral de f(x)
    usando o metodo hit or miss
    Escreva o seu codigo nas proximas linhas
    """
    n = n
    ponto_dentro = 0
    lista_estimativas = []
    total = 1
    
    points = qmc.Sobol(d=2, scramble=True)
    qrpoints = points.random_base2(m=int(np.around(np.log2(n))))
    
    #gerando pontos uniformemente dentro do quadrado [0,1]x[0,1] aplicando a função e checando se está dentro ou nao
    for i in qrpoints:
        ponto = [i[0],i[1]]
        if ponto[1] <= f(ponto[0]) :
            ponto_dentro += 1
            lista_estimativas += [ponto_dentro/total]
        
        else:
            None
        
        total += 1
    """    
    plt.figure(num=0,dpi=120)    
    plt.plot(list(range(len(lista_estimativas))),lista_estimativas)
    plt.yticks(np.arange(min(lista_estimativas), max(lista_estimativas), 0.1))
    """

    return ponto_dentro/len(qrpoints)







def control_variate(n = 30000, Seed = None):
    random.seed(Seed)
    """
    Esta funcao deve retornar a sua estimativa para o valor da integral de f(x)
    usando o metodo control variate
    Escreva o seu codigo nas proximas linhas
    """
    
    N = n
    estimativa = 0
    lista_estimativas = []
    
    points = qmc.Sobol(d=1, scramble=True)
    qrpoints = points.random_base2(m=int(np.around(np.log2(n))))
    
    #para este método utilizamos a função g(x) que aproxima bem a função f(x)
    for i in range(len(qrpoints)):
        estimativa += f(qrpoints[i])- g(qrpoints[i]) + 0.75
        lista_estimativas += [estimativa/(i+1)]
        
    """
    plt.figure(num=0,dpi=120)    
    plt.plot(list(range(len(lista_estimativas))),lista_estimativas)
    plt.yticks(np.arange(min(lista_estimativas), max(lista_estimativas), 0.1))
    """
    

    return float(lista_estimativas[-1])








def importance_sampling(n = 200000, Seed = None):
    random.seed(Seed)
    """
    Esta funcao deve retornar a sua estimativa para o valor da integral de f(x)
    usando o metodo importance sampling
    Escreva o seu codigo nas proximas linhas
    """
    N = n
    estimativa = 0
    lista_estimativas = []
    dist = scipy.stats.beta(0.99,1.27)
    
    #para esta função utilizaremos a distribuição beta com parametros 0.99 e 1.27
    for i in range(1,N+1):
        x = np.random.beta(0.99,1.27)
        estimativa += f(x)/dist.pdf(x)
        lista_estimativas += [estimativa/i]
        #print(f'O progresso está {round((i/N)*100,2)}% completo')
        #descomente a linha acima se o número de pontos passar de 10 mil pois a função demora um pouco
    return lista_estimativas[N-1]

def plot_fx():
    """
    função para plotar o gráfico da função f(x)
    
    """
    xs = [float(i/100) for i in range(int(100))]
    ys = [f(x) for x in xs]
    plt.figure(dpi=120)
    plt.plot(xs,ys)
    plt.title("f(x)");


def encontre_n():
    
    """
    Função para encontrar o N ideal
    Troque a chamada do método pelo desejado
    Pode ser um pouco lenta dependendo do método
    """
    #N inicial
    n=1
    #desvio padrao inicial
    s=0
    erro1 = 1
    lista_estimativas = []
    tolerancia = 0.0005
    #troque abaixo para diferentes métodos
    estimativa = control_variate(n)
    lista_estimativas += [estimativa]
    while erro1 > tolerancia:
        n += 1000
        #troque abaixo para outro método
        estimativa = control_variate(n)
        lista_estimativas += [estimativa]
        m = np.mean(lista_estimativas)
        s = np.std(lista_estimativas)
        #cálculo do erro para o N setado e o desvio-padrão do estimador com N pontos
        erro2 = (1.96**2 * s)/np.sqrt(n)
        erro1 = 2*erro2/m
        print(n)
    return n


def main():
    #Coloque seus testes aqui
    print(crude())
    print(hit_or_miss())
    print(control_variate())
    print(importance_sampling())




if __name__ == "__main__":
    main()