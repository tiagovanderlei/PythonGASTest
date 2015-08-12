__author__ = 'tiagovanderlei'

# modulo utilizado na Parte VI, secao 4

def perimetro(r):
    try:
        return 2*3.14*float(r)
    except:
        print 'O argumento da funcao deve ser numerico'


def area(r):
    try:
        return 3.14*(r**float(2))
    except:
        print 'O argumento da funcao deve ser numerico'

def potencia(x,y=2):
    """ potencia(x, y:default=2) - eleva x a potencia y.
    """
    try:
        return x**y
    except:
        print 'O argumento da funcao deve ser numerico'

def nada():
    pass #break, continue, pass --> pass: The pass statement in Python is used when a statement is required syntactically but you do not want any command or code to execute.