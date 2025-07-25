from datetime import date 
import random
#==========================================================================================================================================================================
#verificador da liberação de financiamento de uma casa
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#print('para saber se nosso banco libera o financiamento da casa para voce digite as informações abaixo:')
#casa = float(input('o valor da casa: '))
#salario = float(input('seu salario mensal: '))
#anos = int(input('em quantos anos voce quer parcela a casa: '))
#meses = (anos * 12)
#parcela = float(casa / meses)
#if parcela <= salario - salario * 0.30:
#    input('seu financiamento foi aceito \nsuas parcelas serão de R${:.2f} \ndurante {} meses '.format(parcela, meses))
#else:
#    print('seu financiamento foi negado')

#==========================================================================================================================================================================
#convesor de numero inteiro para binario, octal e hexadecimal  
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#numero = int(input('digite um numero inteiro'))
#print('''escolha umas das base para conversão:
#[ 1 ] converter para binario
#[ 2 ] converter para octal
#[ 3 ] converter para hexadecimal''')
#opção = int(input('sua escolhar:'))
#if opção == 1:
#    print('{} convertido para binario e igual a: {}'.format(numero, bin(numero)[2:])) 
#elif opção == 2:
#    print('{} convertido para octal e igual a: {}'.format(numero, oct(numero)[2:]))
#elif opção == 3:
#    print('{} convertido para hexadecimal e igual a {}'.format(numero, hex(numero)[2:]))
#else:
#    print('numero invalido tente novamente')

#==========================================================================================================================================================================
#verificador qual numero e maior 
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#primeiro = int(input('primeiro numero: '))
#segundo = int(input('segundo numero: '))
#if primeiro > segundo:
#    print('o numero {} e maior que {}'.format(primeiro, segundo))
#elif segundo > primeiro:
#    print('o numero {} e maior que {}'.format(segundo, primeiro))
#else:
#    print('os dois valores são iquais')
#==========================================================================================================================================================================
#verifica se você precisa se alistar
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# print('para saber se voce precisa se alistar responda as perguntas abaixo' )
# sexo = int(input('qual seu sexo? \n[ 1 ] Masculino \n[ 2 ] Feminino \nresporta: '))
# ano = int(input('escreva o ano que voce nasceu: '))
# atual = date.today().year
# idade = atual - ano
# if sexo == 2 :
#     print('o alistamento militar não e obrigatorio para mulheres voce não precisa se alistar')
# elif idade < 18:
#     falta = 18 - idade
#     print('ainda não precisa se alistar falta {}'.format(falta))
# elif idade == 18:
#     print('esta na hora de voce se alistar')
# else:
#     passou = idade - 18
#     print('voce ja deveria ter se alistado a {} anos se voce ainda não se alistou procure a junta militar mais proxima da sua cidade'.format(passou))
#==========================================================================================================================================================================
#calculadora de media de duas notas
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# primeira = float(input('sua primeira nota:'))
# segunda = float(input('sua segunda nota: '))
# media = (primeira + segunda) / 2
# if media <= 5:
#     print('sua media foi {} infelizmente voce reprovou'.format(media))
# elif media <= 6.9:
#     print('Sua media e {} voce precisa fazer a recuperação'.format(media))
# elif media >= 7.00:
#     print('parabens sua media foi {} voce foi aprovado'.format(media))

#==========================================================================================================================================================================
#verificador de categoria de uma pessoa
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# nascimento = int(input('escreva o ano que voce nasceu para saber em qual categoria voce competi: '))
# atual = date.today().year
# idade = atual - nascimento
# if idade <= 9:
#     print('voce tem {} de idade e ira participa da categoria mirim'.format(idade))
# elif idade <= 14:
#     print('voce tem {} de idade e ira participa da categoria infantil'.format(idade))
# elif idade <= 19:
#     print('voce tem {} de idade e ira participa da categoria junior'.format(idade))
# elif idade <= 20:
#     print('voce tem {} de idade e ira participa da categoria sênior'.format(idade))
# elif idade > 20:
#     print('voce tem {} de idade e ira participa da categoria master'.format(idade))
#==========================================================================================================================================================================
#analisa tres retas para ver se e posivel criar um triangulo
# #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# print('=====================================================================================')
# print('para analisa se 3 retas podem forma um triangulo escreva o tamanho das 3 retas abaixo')
# print('=====================================================================================')
# a = float(input('reta a: '))
# b = float(input('reta b: '))
# c = float(input('reta c: '))

# if a > b and a > c:
#     maior = a
#     if b + c > a:
#         print('sim com essas tres retas voce pode criar um tiangulo')
#         if a == b and a==c:
#             tipo = ('equilátero')
#         elif a == b or a == c:
#              tipo = ('isósceles')
#         else:
#             print('escaleno')
#     else:
#         print('voce não pode forma um triangulo com essas tres retas')
# if b > a and b > c:
#     maior = b
#     if a + c > b:
#         print('sim com essas tres retas voce pode criar um tiangulo ')
#         if a == b and a==c:
#              tipo = ('equilátero')
#         elif a == b or a == c:
#              tipo = ('isósceles')
#         else:
#             print('escaleno')
#     else:
#          print('voce não pode forma um triangulo com essas tres retas')
# if c > a and c > b:
#     maior = c
#     if a + b > c:
#         print('sim com essas tres retas voce pode criar um tiangulo ')
#         if a == b and a==c:
#              tipo = ('equilátero')
#         elif a == b or a == c:
#              tipo = ('isósceles')
#         else:
#             print('escaleno')
#     else:
#          print('voce não pode forma um triangulo com essas tres retas')
#==========================================================================================================================================================================
#calculadora de IMC
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# altura = float(input('sua altura: '))
# peso = float(input('seu peso: '))
# imc = peso/(altura * altura)
# print('seu indice de massa corporal e: {:.1f}'.format(imc))
# if imc < 18.5:
#     print('você esta abaixo do peso ideal')
# elif imc < 25:
#     print('você esta com o peso ideal para sua idade')
# elif imc <= 30:
#     print('você esta com o peso acima do ideal')
# elif imc <=40:
#     print('você esta obeso')
# elif imc > 40:
#     print('você esta com obesidade mórbida')
#==========================================================================================================================================================================
#programa de uma maquina de cartão
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# print('{} LOJAS ALVES {}'.format('='*20,'='*20))
# preço = float(input('valor do produto: '))
# print('formas de pagamentos: \n[1] dinheiro/pix \n[2] debito \n[3] 2x no credito \n[4] 3x no credito')
# pagamento = int(input('digite a forma de pagamento: '))
# if pagamento == 1:
#     print('o valor do produto avista com 10% de descconto vai fica R${}'.format(preço - preço * 0.10))
# elif pagamento == 2:
#     print('o valor do produto no debito com 5% de desconto vai fica R${}'.format(preço - preço * 0.05))
# elif pagamento == 3:
#     print('o valor do produto parcelado em 2x no credito vai se o preço sem desconto R${}'.format(preço))
# elif pagamento == 4:
#     print('o valor do produto parcelado em 3x no credito com juros de 20% vai ficar R${}'.format(preço + preço * 0.20))
#==========================================================================================================================================================================
#jogo de pedra papel e tesoura
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# print('nesse programa você pode jogar pedra papel e tesoura com o computador \npara jogar escolha entre pedra papel e tesoura')
# print('[1] pedra \n[2] papel \n[3] tesoura')
# voce = int(input('sua escolha: '))
# computador = random.randrange(1, 4)
# if voce == 1:
#     a = ('pedra')
# elif voce == 2:
#     a = ('papel')
# elif voce == 3:
#     a = ('tesoura')
# if computador == 1:
#     b = ('pedra')
# elif computador == 2:
#     b = ('papel')
# elif computador == 3:
#     b = ('tesoura')
# print('computador {}'.format(computador))
# print('voce '+a)
# print('computador '+b)
# if voce == computador:
#     print('voces dois escolheram a mesma coisa tente novamente')
# elif voce == 1  and computador == 2:
#     print('computador venceu')
# elif voce == 1 and computador == 3:
#     print('voce venceu')
# elif voce == 2 and  computador == 1:
#     print('voce venceu')
# elif voce == 2 and computador == 3:
#     print('computador venceu')
# elif voce == 3 and computador == 1:
#     print('computado venceu')
# elif voce == 3 and computador == 2:
#     print('voce ganhou')