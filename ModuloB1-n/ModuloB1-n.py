__author__ = 'tiagovanderlei'

# A partir da pagina 8

a='araraquara'
print a.split('a')

print dir(a)   # lista os atributos de um objeto ou classe

class Cachorros:
    __name__='Cachorros'
    pass

cachorros=Cachorros()
print id(cachorros) # retorna inteiro hexa que identifica o objeto

print cachorros
print cachorros.__name__

# self, __init__,

# self.area = x -- atribui x a variavel area: escopo da classe
# self : primeiro argumento na def. da maioria dos metodos de classe: ref. a propria instancia
# self esta implicito como primeiro argumento. Caso nao exista, atributo area passa a existir.
# -- termo self nao eh obrigadorio: 1o. argumento.


# __init__ : construtor da classe

class Cachorros:
    cobertura='pelos'
    alimento='carne'
    patas=4
    habitat='domestico'

    # sempre recebe self (1o. arg) + demais parametros
    def __init__(self, nome):
        self.nome = nome

d1=Cachorros('poodle')
print d1.nome

from random import random

class Sprites:
    """
    documentacao
    """
    def __init__(self,
                 nome,
                 tamanho='grande',
                 cor='amarelo',
                 arestas=5):    # self: sempre 1o. argumento
        """

        :param nome:
        :param tamanho:
        :param cor:
        :param arestas:
        :return:
        """
        self.nome=nome
        self.tamanho=tamanho
        self.cor=cor
        self.arestas=arestas

    def update_position(self):
        self.position = random()*10,random()*10
        print '%s esta agora em %s.' %(self.nome, self.position)



s1=Sprites('Star', 'pequeno', 'vermelho')
print (s1.nome, s1.tamanho, s1.cor, s1.arestas)



s2=Sprites('Star2', arestas=6, cor='azul')
print s2.nome, s2.tamanho, s2.cor, s2.arestas

s1.update_position(), s2.update_position()
print s1.position
print s2.position

print dir(Sprites)
help(Sprites)

print Sprites.__doc__

print Sprites.__init__.__doc__

# __module__ - nome do modulo a que a classe pertence: se no proprio script, retorna 'main'

print Sprites.__module__

from math import sin
print sin.__module__



# ate pag. 40