numero = int(input('Digite um numero para saber se ele e par ou impar: '))
teste = numero % 2
if teste == 0:
   print('o numero escolhido foi {} e ele e um numero par'.format(numero))
else:
   print('seu numero escolhido foi o {} e ele e um numero impar'.format(numero))