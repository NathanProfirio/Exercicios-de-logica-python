import random

#=======================================================================================================================================================================
#jogo das adivinhações
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#print('================================')
#print('o jogo das adivinhações')
#print('================================')
#print("o computador pensou em um numero de 0 a 5 \n")
#sorteio = (int(random.randrange(0, 6)))
#escolha = int(input('escreva um numero de 0 a 5 para tenta adivinha o numero que o computador pensou: '))
#if sorteio == escolha:
 #   print('parabens voce acertou')
#else:
#    print('infelizmente você não acertou você pode tenta novamente')

#=======================================================================================================================================================================
#calculadora de multas
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#print('A velocidade maxima permitida nessa avenida e 80 Km/H e a multa e R$ 7.00 reias por KM/H acima dessa velocidade')
#velocidade = float(input('para saber se seu carro foi multado e o valor da multa digite a velocidade do carro em KM/H: '))
#if velocidade <= 80:
#    print('voce não foi multado')
#else:
#    multa = ((velocidade - 80) * 7.00)
#    print('voce estava a cima da velocidade permitida na avenida foi multado no valor de: R$ {} Reais'.format(multa))

#=======================================================================================================================================================================
#verificador se um numero e impar ou par
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#numero = int(input('Digite um numero para saber se ele e par ou impar: '))
#teste = numero % 2
#if teste == 0:
 #   print('o numero escolhido foi {} e ele e um numero par'.format(numero))
#else:
 #   print('seu numero escolhido foi o {} e ele e um numero impar'.format(numero))

#=======================================================================================================================================================================
#calculadora do valor de uma passagem 
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#print('o valor da passagem e cobrado da seguinte forma ')
#print('50 centavos por KM de distancia do ponto de embargue ate o ponto de desembarque para viagens de ate 200KM de distancia')
#print('para viagens acima de 200 KM o valor e de 45 centavos por diatancia do ponto de embargue ate o ponto de desembarque')
#distancia = (float(input('digite a distancia da viagem em KM para saber o valor da passagem: ')))
#if distancia <= 200:
#    print('o valor da sua passagem sera de R$ {:.2f} reais'.format(distancia * 0.50))
#else:
 #   print('o valor da sua passagem sera de R$ {:.2f} reais'.format(distancia * 0.45))

#=======================================================================================================================================================================
#verificador se um ano e bissexto ou não
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#ano = int(input('escreva um ano para saber se ele e bissexto: '))
#if ano % 4 == 0 and ano % 100 or ano % 400 == 0:
#    print('o ano {} e bissexto'.format(ano))
#else:
#    print('o ano {} não e bissexto'.format(ano))

#=======================================================================================================================================================================
#verificador qual numero e maior e qual e o menor 
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#a = int(input('escreva numeros para saber qual e o maior e o menor numero'))
#b = int(input('eccreva numeros para saber qual e o maior e o menor numero'))
#c = int(input('escreva numeros para saber qual e o maior e o menor numero'))
###teste do maior numero####
#if a > b and a > c:
#    maior = a
#if b > a and b > c:
#    maior = b
#if c > a and c > b: 
#    maior = c
#print(maior)
###teste do menor numero###
#if a < b and a < c:
#    menor = a
#if b < a and b < c:
#    menor = b
#if c < a and c < b:
#    menor = c
#print('o menor numero e o: {} \ne o menor numero e o: {}'.format(menor, maior))

#=======================================================================================================================================================================
#calculadora de aumento de salario
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#print('os salarios dos funcionarios vai ter um aumento')
#print('o aumento dos funcionarios que ganham ate R$1250 vai ser de 15% \nja os funcionario que quanha mais de R$1250 vai se de 10%\n')
#print('para saber qual o aumento do seu salario digite seu salario atual abaixo \n=========================')
#salario = float(input('salario atual: '))
#if salario <= 1250:
#    print('o aumento do seu salario sera de {}'.format('15%'))
#    print('seu salario novo e: R${:.2f}'.format(salario * 0.15 + salario))
#else:
#    print('o aumento do seu salario sera de {}'.format('10%'))
#    print('seu salario novo e: R${:.2f}'.format(salario * 0.10 + salario))

#=======================================================================================================================================================================
#verifica se tres retas forma um triangulo
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

print('para analisa se 3 retas podem forma um triangulo escreva o tamanho das 3 retas abaixo')
print('=====================================================================================')
a = float(input('reta a: '))
b = float(input('reta b: '))
c = float(input('reta c: '))
if a > b and a > c:
    maior = a
    if b + c > a:
        print('sim com essas tres retas voce pode criar um tiangulo')
    else:
        print('voce não pode forma um triangulo com essas tres retas')
if b > a and b > c:
    maior = b
    if a + c > b:
        print('sim com essas tres retas voce pode criar um tiangulo ')
    else:
         print('voce não pode forma um triangulo com essas tres retas')
if c > a and c > b:
    maior = c
    if a + b > c:
         print('sim com essas tres retas voce pode criar um tiangulo ')
    else:
         print('voce não pode forma um triangulo com essas tres retas')
        