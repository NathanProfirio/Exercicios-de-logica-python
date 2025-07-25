import random
import math

#============================================================================================================================================================================================
#função fazer uma linha

def linha():
    print("=" * 40)

#função de limpar o terminal    
def limpador_de_tela():
    print("\n"*10)

#============================================================================================================================================================================================
#calculadora de soma sequencial
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#  numeros_digitados = 0
# soma = 0

# print("escreva os numeros que você que soma para mostra o resultado da soma digite (999)")
# while True:
#     numero = int(input("Escreva um número: "))
    
#     if numero == 999:
#         break

#     numeros_digitados += 1
#     soma += numero

# print(f"Você digitou um total de {numeros_digitados} numeros e a soma desses numeros e {soma} ")

#============================================================================================================================================================================================
#Tabuada de multiplicção de qualque numero
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# while True:
#     print("Digite um numero pra ver a tabuada de multiplicação desse numero")
#     print("Para finalizar digite um valor negativo")
#     numero = int(input("Escolha um numero: "))
#     linha()
#     if numero > 0:
#         for tabuada in range(1, 11):
#             print(f"{tabuada} x {numero} = {tabuada * numero}")
#     else:
#         limpador_de_tela()
#         linha()
#         print("Programa finalizado obrigado")
#         linha()
#         break

#============================================================================================================================================================================================
#jogo de impar ou par
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# print(f"\n{"="*100}\n\nPara jogar Par ou Impar com o computado escolha um numero de 0 a 10 e depois escolha par ou impar \n\n{"="*100}")
# vitorias = 0
# while True:
#     print("\n")
#     numero_usuario = int(input("escolha um numero: "))
#     limpador_de_tela()
#     linha()
#     escolha = int(input("Você que Impar ou Par ? \n[1] Impar \n[2] Par \nSua escolha: "))
#     linha()
#     limpador_de_tela()

#     numero_computador = random.randrange(1, 11)
#     soma = numero_usuario + numero_computador
#     resto_da_divisao = soma % 2 
    
#     linha()
#     print(f"Você jogou {numero_usuario} e o computador jogou {numero_computador} o total foi {soma}")
    
#     if escolha == 1:
#         if resto_da_divisao == 1:
#             print("Voce venceu")
#             vitorias += 1
#             linha()
#         elif resto_da_divisao == 0:
#             print("Você perdeu ")
#             linha()
#             break
#     elif escolha == 2:
#         if resto_da_divisao == 1:
#             print("Você perdeu")
#             linha()
#             break
#         elif resto_da_divisao == 0:
#             print("Você venceu")
#             vitorias += 1
#             linha()
#     else:
#         print("Nùmero invalido")
#         linha()

# print(f"Final do jogo Você ganhou {vitorias} vezes")
# linha()

#============================================================================================================================================================================================
#cadrastro de pessoas
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# maiores_de_18 = 0
# homens = 0
# mulheres_menores_de_20 = 0

# while True:
#     linha()
#     print("cadrastre uma pessoa")
#     linha()
#     idade = int(input("idade: "))
#     sexo = " "
#     while sexo not in "MF":
#         sexo = str(input("Qual o sexo? \n[F] Feminino \n[M] Masculino \nResposta: ")).strip().upper()[0]
#     verificaçao = " "
#     while verificaçao not in "SN":
#         verificaçao = str(input("Você que continua responda com [S/N] \nResposta: ")).strip().upper()[0]
#     if idade > 18:
#         maiores_de_18 += 1 
#     if sexo == "M":
#         homens += 1
#     if sexo == "F":
#         if idade < 20:
#             mulheres_menores_de_20 += 1
#     if verificaçao == "N":
#         break

# print(f"Pessoas com mais de 18 anos: {maiores_de_18}")
# print(f"Quantidades de Homens cadrastrados: {homens}")
# print(f"mulheres com menos de 20 anos: {mulheres_menores_de_20}")

#============================================================================================================================================================================================
#progama de um caixa eletronico 
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# soma = 0
# mais_de_mil = 0
# nome_mais_barato = ""
# valor_mais_barato = 0
# primeiro_loop = 1
# while True:
#     nome = str(input("Nome do produto: "))
#     valor = float(input("Valor do produto: "))
#     soma += valor
#     if valor > 1000:
#         mais_de_mil += 1
    
#     if primeiro_loop == 1:
#         valor_mais_barato = valor
#         nome_mais_barato = nome
#         primeiro_loop += 1

#     if valor < valor_mais_barato:
#         nome_mais_barato = nome
#         valor_mais_barato = valor
 
#     verificaçao = str(input("Você que continua [S/N] \nResposta: ")).strip().upper()[0]
#     if verificaçao == "N":
#         print(f"total das compras: R${soma} \nTemos {mais_de_mil} produtos que custando mais de R$1000  \nProduto mais barato foi {nome_mais_barato} Que custa: R${valor_mais_barato} ")
#         break

#============================================================================================================================================================================================
#sistema de saque de um caixa eletronico
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# linha()
# print("Caixa Eletronico")
# linha()
# print("\n")

# notas_de_50 = 0
# notas_de_20 = 0
# notas_de_10 = 0
# notas_de_1 = 0

# saque = int(input("Qual valor você desseja sacar R$"))
# total = saque
# while total >= 50:
#     total -= 50
#     notas_de_50 += 1

# while total >= 20:
#     total -= 20
#     notas_de_20 += 1

# while total >= 10:
#     total -= 10
#     notas_de_10 += 1

# while total >= 1:
#     total -= 1
#     notas_de_1 += 1

# if notas_de_50 > 0:
#     print(f"Total de {notas_de_50} cedulas de R$50")
# if notas_de_20 > 0:
#     print(f"Total de {notas_de_20} cedulas de R$20")
# if notas_de_10 > 0:   
#     print(f"Total de {notas_de_10} cedulas de R$10")
# if notas_de_1 > 0:
#     print(f"Total de {notas_de_1} cedulas de R$1")
# linha()
# print("Saque concluido volte sempre")
# linha()
