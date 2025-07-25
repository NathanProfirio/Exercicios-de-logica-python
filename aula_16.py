import random 

#============================================================================================================================================================================================
#Escreve um numero para ver ele escrito por extenso
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# numeros = ("Zero","Um","Dois","Três","Quatro","Cinco","seis","Sete","Oito","nove","Dez","Onze","Doze","Treze","Quatorze","Quinze","Dezesseis","Dezessete","Dezoito","Dezenove","Vinte")
# while True:
#     escolha = int(input("Digite um número de 0 a 20: "))
#     if escolha <= 20 and escolha >= 0:
#         print(numeros[escolha])

#============================================================================================================================================================================================
#verificador de posição de um time
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# times = ("Palmeira","Flamengo","Cruzeiro","Bragatino","Ceará sc","Bahia","Fluminense","Corinthians","Mirassol","Atletico","Botafogo","São paulo","Vasco da gama","Fortaleza","Internacional","EC Vitoria","Grêmio","Juventude","Santos","Sport Recife")  
# print(times)
# print("\n")
# print(times[:5])
# print("\n")
# print(times[-4:])
# print("\n")
# print(sorted(times))
# print("\n")    
# flamengo = times.count("Flamengo") + 1
# print(f"O flamengo esta na posição º{flamengo} da tabela do brasileirão")

#============================================================================================================================================================================================
#sortei 5 numeros e verifica qual o menor e qual o maior numero sorteado
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# maior_numero = 0
# menor_numero = 0
# primeiro_loop = 0
# numeros = (random.randrange(1,11),random.randrange(1,11),random.randrange(1,11),random.randrange(1,11),random.randrange(1,11))
# for m in numeros:
# ##teste do menor numero 
#     if primeiro_loop == 0:
#         menor_numero = m
#         primeiro_loop += 1
#     if m < menor_numero:
#         menor_numero = m

# ##teste do maior numero
#     if primeiro_loop == 1:
#         maior_numero = m
#         primeiro_loop += 1
#     if m > maior_numero:
#         maior_numero = m
# print(numeros)
# print(f"O menor numero sorteado foi o: {menor_numero}")
# print(f"O maior numero sorteado foi o: {maior_numero}")

#============================================================================================================================================================================================
