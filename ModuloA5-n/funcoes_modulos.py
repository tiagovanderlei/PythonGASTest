__author__ = 'tiagovanderlei'

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

