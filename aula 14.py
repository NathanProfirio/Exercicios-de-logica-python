import random 
import os

#==========================================================================================================================================================================
#menu de escolha de sexo (masculino e feminino)
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# sexo = 'a'
# while sexo != 'M' and sexo != 'F':
#    print("Para continuar digite seu sexo o programa so aceita [F] para Feminino e [M] para masculino")
#    print("="*80)
#    sexo = str(input('[M] masculino \n[F] feminino \nresportas: ')).upper()
# print('obrigado sua resposta foi {}'.format(sexo))

#==========================================================================================================================================================================
#jogo das adivinhaçoes
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# print("{} jogo das advinhações {} \nO computador vai escolher um número de 1 a 10 tente adivinha qual número ele escolheu".format("="*30,"="*30))
# computador = 0
# eu = 1
# while computador != eu:
#     computador = random.randrange(1,11)
#     eu = int(input("seu palpite: "))
#     print("="*50)
#     print("o computador escolheu {} e você escolheu {}".format(computador, eu))
#     if computador == eu:
#             print("parabens você acertou")
#     elif eu > 10:
#         print("\n{} \nresposta invalida escolha um número entre 1 e 10\n{}".format("="*50,"="*50))
#     else:
#         print("Você errou tente novamente\n ".format("="*30))
# print("*="*50)

#==========================================================================================================================================================================
#calculadora de soma e multiplicação e verificação de qual o maior e menor numero
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# opçao = 8
# while(opçao > 5 or opçao <=0):
#     print("Escolha dois numeros em sequencia escolha o que você que fazer com os dois numeros")
#     primeiro = float(input("primeiro número: "))
#     segundo = float(input("Segundo número: "))
#     print("{} MENU {}".format("="*20,"="*20))
#     print("[1]Somar \n[2]Multiplicar \n[3]Maior E Menor \n[4]Novos números \n[5]Sair do programa")
#     opçao = int(input("resposta: "))
#     if opçao > 5 or opçao <= 0:
#         print("\n" * os.get_terminal_size().lines)
#         print("{} \nOpção invalida escolha uma opção valida \n{}".format("="*50, "="*50))
#     if opçao == 1:
#         print("{} RESPOSTA {}".format("="*20,"="*20))
#         print("{} + {} = {}".format(primeiro, segundo, primeiro + segundo))
#         print("\n"*3)
#         opçao = 8

#     elif opçao == 2:
#         print("{} RESPOSTA {}".format("="*20,"="*20))
#         print("{} x {} = {}".format(primeiro, segundo, primeiro * segundo))
#         opçao = 8

#     elif opçao == 3:
#         if primeiro > segundo:
#             print("o maior número digitado foi o {} ".format(primeiro))
#             print("o menor número digitado foi o {} ".format(segundo))
#             opçao = 8
#         else:
#             print("o maior número digitado foi o {}".format(segundo))
#             print("O menor número digitado foi o {}".format(primeiro))
#             opçao = 8

#     elif opçao == 4:
#         opçao = 8
#         print("\n" * os.get_terminal_size().lines)
#     elif opçao == 5:
#         print("saindo!!!!!!! \ntchau")

#==========================================================================================================================================================================
#Calculadora de fatorial de um numero
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# print("{} \nEscreva um número para saber o fatorial dele \n{} ".format("="*50,"="*50))
# fatorial = 1
# numero = int(input("Número escolhido: "))
# contagem = numero
# while contagem > 0:
#     fatorial = contagem * fatorial
#     if contagem == 1:
#         print("{} = {}".format(contagem, fatorial))
#         contagem -= 1
#     else:
#         print("{}x".format(contagem),end='')
#         contagem -= 1
# print("O fatorial de {}! é {}".format(numero, fatorial))

#==========================================================================================================================================================================
#Calculadora de termos de uma PA
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# print("{} \n10 TERMOS DE UMA PA \n{}".format("="*50,"="*50))
# primeiro = int(input("Primeiro termo: "))
# razao = int(input("Razão: "))
# contagem = 10
# resultados = primeiro
# while contagem >0:
#     if contagem == 1:
#         print(" {} ".format(resultados))
#         contagem = int(input("Voce que mostra mais quantos termos: "))
        
#     else:
#         print(" {} >".format(resultados),end='')
#         resultados = razao + resultados
#         contagem -= 1

#==========================================================================================================================================================================
#sequencia de fibonacci
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# print("escolha a quantos termos voce que ver da sequencia de fibonacci")
# a = 0
# b = 1
# soma = 0
# contador = 3
# termos = int(input("Números de termos: "))
# print("{} > {}".format(a,b),end='')
# while termos >= contador:
#     soma = a + b
#     print(" > {}".format(soma),end='')
#     a = b
#     b = soma
#     contador += 1
# print(" > FIM")

#==========================================================================================================================================================================
#calculadora de soma sequencial
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# print("essa e uma calculador de soma sequencia o que significa que ela so vai para de pedir numeros quando o usuario digitar 999")
# loop = 0
# quantidade_digitada = 0
# soma = 0
# while loop <= 2:
#     numero = int(input("numero: "))
#     if numero != 999:
#         soma += numero
#         quantidade_digitada += 1
#     else:
#         print("Você digitou {} números e o resultado da soma de todos os número foi de {}".format(quantidade_digitada,soma))
#         loop += 3

