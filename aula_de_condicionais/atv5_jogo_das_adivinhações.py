import random


print('================================')
print('o jogo das adivinhações')
print('================================')
print("o computador pensou em um numero de 0 a 5 \n")
sorteio = (int(random.randrange(0, 6)))
escolha = int(input('escreva um numero de 0 a 5 para tenta adivinha o numero que o computador pensou: '))
if sorteio == escolha:
   print('parabens voce acertou')
else:
   print('infelizmente você não acertou')