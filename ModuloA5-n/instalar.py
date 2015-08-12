__author__ = 'tiagovanderlei'

# exemplo instalar.py

import os
import webbrowser

def instalar():
    comando=os.system

    nome=raw_input('Seu nome: ')
    dir = './dirInstalacaoEx%s' %nome
    comando('mkdir '+dir+'')
    comando('cp ./circulos.py '+'%s/circulosInstalado.py' %dir)
    # abrir=os.startfile   --- aparentemente startfile so no windows
    #abrir('./LICENSE')

    webbrowser.open(os.path.realpath("./LICENSE"))

def desinstalar():
    comando=os.system
    comando('rm -rf %s' %'dirInstalacaoEx*')
