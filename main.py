'''''
def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
if __name__ == '__main__':
    print_hi('PyCharm')
print('==' * 15)

import math
num = int(input('Entre com um numero:'))
print('A raiz quadrada de: {} é: {}'.format(num, math.sqrt(num)))
print('==' * 15)

nr = int(input('Entre com o numero: '))
bs = int(input('Entre com o valor da base: '))
log = math.log(nr, bs)
print('O log de: {} na base {}  será: {}'.format(nr, bs, log))
'''
'''
frase = 'Curso em Video Python'
print(frase)
div = frase.split()
print(div[3])

#print("-".join(frase))

print(frase[:21])
print(frase[:5])

print(len(frase))

'''
'''
nome = str(input('Entre com um nome:'))
#print(nome)
print(nome.upper())
print(nome.lower())
print(len(nome), 'letras ao todo')
letras = int(len(nome))
espacos = nome.count(' ')
print('Seu nome tem um total de {} letras e {} espaços'.format((letras - espacos), espacos))
div = nome.split()
print(div[0])
print(len(div[0]))

num = str(input('Digite um numero: '))
divi = num.split()
print(divi[0])
'''
'''
nome = str(input('Qual é o seu nome? :'))
if nome == 'Gerson':
    print('Que nome lindo!')
else:
    print('Seu nome é tão normal!')
    print('Prazer em conhece-lo {}!'.format(nome))
'''

'''
md1 = float(input('\33[1:33:40mEntre com a primeira nota: '))
md2 = float(input('Entre com a segunda nota: '))
media = (md1 + md2)/2
print('\33[1:33:40mA sua média foi: {}\33[m'.format(media))
if media >= 6:                                     # Condição composta!
    print('\33[1:33:40mA sua média foi boa. PARABÉNS!\33[m')
else:
    print('\33[1:33:40mA sua média não foi boa. \33[34mEstude mais!\33[m')

print('\33[1:33:40mParabéns!\33[m'if media >= 6 else '\33[1:33:40mSe esforçe mais!\33[m') # Condição simplificada!

'''

print('\33[3:34:40mOlá Mundo Python!\33[m')
a = 5
b = 8
print('Os valores são: \33[1:31m{} \33[m e \33[1:33m{}'.format(a, b))


nome = 'Gerson Pereira'
cores = {'limpa':'\33[m ',
         'azul':'\33[34m',
         'amarelo':'\33[33m',
         'pretobranco':'\33[7;30m'}
print('{}Prazer em te conhecer {}{}{}!!'.format(cores['limpa'],cores['amarelo'], nome, cores['limpa']))









