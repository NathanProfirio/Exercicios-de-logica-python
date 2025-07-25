import time 
from datetime import date 
#==========================================================================================================================================================================
#contagem regressiva para o ano  novo
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# for c in range(10, -1, -1):
#     time.sleep(1)
#     print(c)
# print('{} feliz ano novo {}'.format(10 * '*', 10 * '*'))

# for par in range(2, 51, 2):
#     print(par, end=' ')

# soma = 0
# contagem = 0
# for c in range(1, 501, 1):
#     if c % 2 == 1:
#         if c %  3 == 0:
#             contagem = contagem + 1
#             soma = soma + c
# print('existem {} numeros impares entre 0 e 500 que são multiplos de 3 e a soma de todos os numeros e {}'.format(contagem, soma))
#==========================================================================================================================================================================
#tabuada de multiplicação de qualqeur numero
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# print('digite um numero para ver a tabuada de multiplicação desse numero')
# numero = int(input('o numero: '))
# print('='*20)
# for t in range(1, 11, 1):
#     print('{}x{}={}'.format(numero, t,numero * t))
# print('='*20)

# soma = 0
# for p in range(1, 7, 1):
#     numero = int(input('escreva um numero: '))
#     if numero % 2 == 0:
#         soma = soma + numero
# print(soma)

# primeiro = int(input('primeiro termo'))
# razão = int(input('razão da PA'))
# decimo = primeiro + (10 + 1 ) * razão
# for c in range(primeiro, decimo, razão):
#     print(c)
#==========================================================================================================================================================================
#verificador de textos polindromo
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# print('escreva um texto para saber se ele e um palindromo')
# texto = str(input('texto: ')).upper().split()
# junta = ''.join(texto)
# inverso = ''
# for t in range(len(junta) -1, -1, -1):
#     inverso = inverso + junta[t]
# print('o inverso de {} e {}'.format(junta, inverso))
# if inverso == junta:
#     print('temos um políndromo')
# else:
#     print('a frase digitada não e um polídromo')
#==========================================================================================================================================================================
#ler a idade de varias pessoas e verifica quantas pessoas são maiores e menores de idade
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# menor = 0
# maior = 0
# ano_atual = date.today().year
# for r in range(1, 8, 1):
#     nascimento = int(input('ano do nascimento: '))
#     idade = ano_atual - nascimento
#     if idade <= 21:
#         menor = menor + 1
#     else:
#         maior = maior +1
# print('tem {} pessoas maiores de idade e tem {} pessoas menor de idade '.format(maior, menor))
#==========================================================================================================================================================================
#ler o nome de 5 pessoas e no no final mostra a pessoa mais pesada e a pessoa masi leve 
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# maior = 0
# meno = 0 
# for p in range(1, 6):
#     peso = float(input('escreva o peso da {}° pessoa: '.format(p)))
#     if p == 1:
#         maior = peso
#         menor = peso
#     else:
#         if peso > maior:
#           maior = peso
#         if peso < menor:
#           menor = peso
# print('o peso da pessoa mais pesada e {}'.format(maior))
# print('o peso da pessoa mais leve e {}'.format(menor))

#==========================================================================================================================================================================
#program ler nome idade e sexo de 4 pessoas e mostra a media de idade das pessoas a idade do homem mais velho e quantas mulhere tem menos de 20 anos
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# media = 0
# homem_mais_velho = 0
# nome_mais_velho = 0
# mulher_menor_de_20 = 0
# for t in range(1, 5):
#     nome = str(input('nome da {}° pessoa: '.format(t)))    
#     idade = int(input('qual a idade da {}° pessoa: '.format(t)))
#     media = media + idade
#     sexo = int(input('qual o sexo da {}° pessoa \n[1] Masculino \n[2] Feminino \nresposta: '.format(t)))
#     print('\n')
#     if t == 1:
#         if sexo == 1:
#             homem_mais_velho = idade
#             nome_mais_velho = nome
#         if idade < 20:
#                 mulher_menor_de_20 = mulher_menor_de_20 + 1
#     else:
#         if sexo == 1:
#             if idade > homem_mais_velho:
#                 homem_mais_velho = idade
#                 nome_mais_velho = nome
#         if sexo == 2:
#             if idade < 20:
#                 mulher_menor_de_20 = mulher_menor_de_20 + 1
    
# print('A media da idade das pessoas e {}'.format(media/4))
# print('A idade do homem mais velho e {} e seu nome e {}'.format(homem_mais_velho, nome_mais_velho))
# print('A quantidade de mulheres que tem menos de 20 anos e: {}'.format(mulher_menor_de_20))
#==========================================================================================================================================================================

