__author__ = 'tiagovanderlei'

###### Estudo do conteudo do pdf ModuloA - ate a pagina 43. As demais nao sao consideradas essenciais neste momento.

def f(x):
    return x**2

print f(4)

def elevar(x,y):
    return x**y

print elevar(2,5)


# toma elementos do parenteses como tupla

def impressora(*argumentos):
    return argumentos

print impressora(1,2,3)

def somatoria(*argumentos):
    soma = 0
    for x in argumentos:
        soma += x
    return soma

# tratamento de erros
def somatoria_(*argumentos):
    soma = 0
    for x in argumentos:

        try:
            soma += x
        except:
            print 'Argumento-', x, '-foi ignorado na soma.'

    return soma


print somatoria_(3,7,'teste',9,2)

print elevar(f(3), 4)

# default, caso parametro nao informado
def user(nome="guest"):
    print "Usuario: %s" %nome

user("Joao")

# map -- qdo se tem uma funcao e uma seq. de elementos de entrada p. funcao: retorna lista el.

def quadrado(termo):
    return termo**2

elementos=[1,4,9,16,25,36]
listaRetorno=map(quadrado,elementos)

print listaRetorno

# outro exemplo com lista nao algebrica
orcamento={'asa':1200, 'combustivel':200, 'motor':4500}

def cambio(componente):
    print componente[0],'R$ ',componente[1]
    print componente[0],'U$ ',componente[1]/3.
    print '\n'

map(cambio,orcamento.items())

#print orcamento.items() -- lista de tuplas

def soma(alfa,beta):
    return alfa+beta

print reduce(soma,[1,2,3])

def eleva(base, expoente):
    return base**expoente

print reduce(eleva,[4,3,2,1])

# list comprehensions

print [x**2 for x in [1,2,3]]

print ['%ss' %nome for nome in ['Proclise','Jilo']]

    # com sequencias
x = ((4, 5, 6), (7, 8, 9), (5, 6, -7))
print [a+b+c for (a,b,c) in x]

    # com map
def metade(val):
    return val/2


print map(metade, [k*2 for k in [66,77,88,99]])

print [metade(k*2) for k in [66,77,88,99]]

# side effect:efeito colateral (print, concatenacao) != valor de retorno

# Modulos

import sys
for i in sys.path:
    print i

import circulos

print circulos.perimetro(2)
print circulos.area(2)
print circulos.potencia(2,5)
print circulos.nada()
print circulos.potencia.__doc__ # doc definido na propria funcao

# importa funcoes:
from circulos import perimetro,area # ou import *
print perimetro(2)
print area(2)

# modulos prontos python (googlar, p/ nao reinventar a roda):

from math import pi, sin, cos, log, log10, pow

print pi
print sin(pi)
print cos(pi)
print sin(cos(sin(pi)))
print log(1)
print log10(2)
print pow(2,4)
print pow.__doc__

# modulo cmath - similar a math, mas p. trabalhar com numeros complexos

# Escopo

# hierarquia: locais (funcoes, classes e modulos), globais (ao longo do programa), built-ins (utilizados nativamente)


def volume(inc):
    global t            ## forca uma variavel local ser definida como global
    t=0.6
    return (pi*(t+inc)**3)/3

print "volume", volume(0.4)
print t

# para evitar confusao, pode-se utilizar math.sin, caso haja funcao definida pelo usuario com nome sin

# Arquivos

# modos de abertura:
    # r - abre para ler
    # a - abre somente p. escrita c/ concatenar
    # w - abre somente p. escrita s/ concatenar

# open(endereco/nome arq.extensao, modo abertura)

# /Users/tiagovanderlei/Documents/git/PythonGASTest/ModuloA5-n/novo_arq.txt

abertura=open('./novo_arq.txt', 'w')
abertura.write('%s - %i\n' %('Tabela de dolares', 123))
abertura.close()

abertura=open('./novo_arq.txt', 'a')
abertura.write('.. append ..\n')
abertura.close()

# leitura


abertura=open('./novo_arq.txt', 'r')

#print abertura.readline()   # linha a linha
print '---'
for x in abertura.readlines():   # lista de linhas do arquivo
    print x


import os
a = os.system

print a('ls') # executa comando :: terminal

from instalar import instalar,desinstalar

instalar()
desinstalar()

##### Ate pagina 43 somente
