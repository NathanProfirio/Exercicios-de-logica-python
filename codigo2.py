import math
import random

#=======================================================================================================================================================================
#mostra a parte inteira de um float
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#numero = float(input('escreva um numero real'))
#print('a parte inteira do seu numero real e {:.0f}'.format(math.trunc(numero)))

#=======================================================================================================================================================================
#calculo do comprimento da hiportenusa usando cateto oposto e cateto adjacente
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#print('para saber o comprimento da hiportenusa digite o comprimento do cateto oposto e do cateto adjacente')
#oposto = float(input('escreva o valor do cateto oposto: '))
#adjacente = float(input('escrevs o valor do cateto adjacente: '))
#print('a valor da sua hipotenusa e {}'.format(math.hypot(oposto, adjacente)))

#=======================================================================================================================================================================
#calculador usando o angulo para saber o seno consseno e a tangente desse angulo
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#print ('digite um angulo para saber o seno consseno e a tangente desse angulo')
#angulo = float(input('escreva um angulo: '))
#radiando = float(math.radians(angulo))
#print(' seno: {:.2f} \n cosseno: {:.2f} \n tangente: {:.2f}'.format(math.sin(radiando),math.cos(radiando),math.tan(radiando)))

#=======================================================================================================================================================================
#sorteio de nomes de pessoas
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# print('escreva o nome de 4 pesssoas para sortea uma')
# a = str(input('primeiro nome: '))
# b = str(input('segundo nome: '))
# c = str(input('terceiro nome: '))
# d = str(input('quarto nome: '))
# nome =[a, b, c, d]
# print('o nome da pessoa sorteada e: {} '.format(random.choice(nome)))

#=======================================================================================================================================================================
#sorteio de ordem de apresentação
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#print('para sorte uma ordem de apresentação digite o nome de 4 pessoas')
#a = str(input('primeiro nome: '))
#b = str(input('segundo nome: '))
#c = str(input('terceiro nome: '))
#d = str(input('quarto nome: '))
#nomes = [a, b, c, d]
#random.shuffle(nomes)
#print('a ordem de apresentação sera:')
#print(nomes)

#=======================================================================================================================================================================
#digite seu nome para ver ele em maiusculo e minusculo quantidades de letras e quantas letras tem seu primeiro nome
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#nome = str(input('escreva seu nome: ')).strip()
#print('seu nome em minusculo e: {}'.format(nome.lower()))
#print('seu nome em maiusculo e: {}'.format(nome.upper()))
#print('seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
#print('seu primeiro nome tem {} letras'.format(nome.find(' ')))
#separa = (nome.split())
#print('seu primeiro nome e {} e ele tem {}  letras'.format(separa[0], len(separa[0])))

#====================================================================================================================================================================
#escreva um numero para ver sua unidade, dezena, centena e milhar 
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# numero = str(input('escreva um numero de 0 a 9999: '))
# print('unidade {} \ndezena {} \ncentena {} \nmilhar {}'.format(numero[3], numero[2], numero[1], numero[0]))

#=======================================================================================================================================================================
#verificador se o ultimo nome de uma cidade e santo
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# cidade = str(input('escreva o nome de uma cidade: ')).strip()
# print(cidade[:5].upper() == 'SANTO')

#=======================================================================================================================================================================
#verifica se seu nome tem silva
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# nome = str(input('escreva seu nome completo ')).strip()
# print('seu nome tem silva? \n{}'.format('SILVA' in nome.upper()))

#=======================================================================================================================================================================
#conta quantas vezes aparece a letra A e qual a posição da primeira e ultima aparição da letra A
# #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#  
#frase = str(input('escreva uma frase: ')).strip().upper()
#print('na sua frase a letra A aparece {} vezes'.format(frase.count('A')))
#print('a primeira vez a letra A e na posiçao {}'.format(frase.find('A') + 1))
#print('a ultima vez que aparece a letra A e na posição {}'.format(frase.rfind('A') + 1))

#=======================================================================================================================================================================
#mostra seu primeiro e ultimo nome
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# nome = str(input('escreva seu nome: ')).strip()
# separaçao = (nome.split())
# print('seu primeiro nome e {}'.format(separaçao[0]))
# print('seu ultimo nome e {}'.format(separaçao[len(separaçao)-1]))

#=======================================================================================================================================================================

