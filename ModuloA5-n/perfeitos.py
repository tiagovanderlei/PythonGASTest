__author__ = 'tiagovanderlei'

#perfeitos.py

n=int(raw_input('Digite o numero a ser testado: '))
teste=0

for i in range(1,n):
    if(n%i == 0):
        teste+=i

if (teste == n):
    print n, 'eh um numero perfeito'
else:
    print n, 'nao eh um numero perfeito'