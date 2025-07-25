#ler o nome de uma pessoa e mostra o nome da pessoa invetido a quantidade de letras que tem o nome e a primeira  e a ultima letra do nome
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# nome = (input("Escreva seu nome: ")).strip().lower()
# idade = (input("Escreva sua idade: "))
# nome_invertido = nome[::-1]
# numeros_de_letras = len(nome)
# if nome and idade:
#     print(f"Seu  nome e {nome}")
#     print(f"Seu nome invetido e {nome_invertido}")
#     print(f"Seu nome tem {numeros_de_letras} letras")
#     print(f"A primeira letra do seu nome e {nome[0]}")
#     print(f"A ultima letra do seu nome e {nome[-1]}")
# else:
#     print("Desculpe, você deixou campos vazios")

#=========================================================================================================================================================
#verifica se um numero e impar ou par
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# numero = input("Escreva um numero: ")
# if numero.isdigit():
#     par_ou_impar = int(numero) % 2
#     if par_ou_impar == 0:
#         print(f"O numero que você digitou foi o {numero} ele e Par")

#     elif par_ou_impar == 1:
#         print(f"O numero que você digitou foi o {numero} ele e Impar")
# else:
    # print("Você não digitou um número inteiro")

#=========================================================================================================================================================
#programa que pergunta a hora e da bom dia boa tarde e boa noite
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# hora = input("Que horas são: ")
# if hora.isdigit():
#     int_hora = int(hora)
#     if int_hora >= 0 and int_hora <= 11:
#         print("Bom dia")
#     elif int_hora <= 17:
#         print("Boa tarde")
#     elif int_hora <= 23:
#         print("Boa noite") 
#     elif int_hora < 0 or int_hora > 23:
#         print(f"Hora invalida ")
# else:
#     print("Valor invalido digite apenas numeros inteiro")

#=========================================================================================================================================================
#escreva seu nome para saber se o tamanho do seu nome e pequeno normal ou grande
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# nome = input("Escreva seu primeiro nome: ")
# quantidade_de_letras = len(nome)
# if quantidade_de_letras > 1:
#     if quantidade_de_letras <= 4:
#         print(f"Seu nome tem {quantidade_de_letras} letras ele é curto")
#     elif quantidade_de_letras <= 6:
#         print(f"Seu nome tem {quantidade_de_letras} letras ele é normal")
#     elif quantidade_de_letras > 6:
#         print(f"Seu nome tem {quantidade_de_letras} letras ele é grande")
# else:
#     print("Digite mais de uma letra")

#=========================================================================================================================================================

# nome = input("Escreva seu nome: ")
# numeros_de_letras = len(nome)
# contador = 0
# while contador < numeros_de_letras:
#     print(f"*{nome[contador]}",end="")
#     contador += 1
# print("\n")

#=========================================================================================================================================================

acertos = ""
palavra_secreta = "geladeira" 
tentativas = 0

while True:

    letra_do_usuario = input("\nDigite uma letra: ")
    tentativas += 1
    if len(letra_do_usuario) > 1:
        print("Digite apenas uma letra")
        continue

    if letra_do_usuario in palavra_secreta:
        acertos += letra_do_usuario
            
    palavra_formatada = ""

    for letra_secretas in palavra_secreta:
        if letra_secretas in acertos:
            palavra_formatada += letra_secretas
        else:
            palavra_formatada += "*"
    print(f"Palavra: {palavra_formatada}")
    if palavra_formatada == palavra_secreta:
        print("\n"*50)
        print(f"{'='*50}\nparabens você ganhou a paravra era {palavra_formatada}\n{'='*50   }")
        break

#=========================================================================================================================================================

# lista = []
# sair = 0


# while sair == 0:
#     print("Selecione uma opção \n[1] Adicionar item \n[2] Apagar item \n[3] Ver lista \n[4] Sair")
#     opcao = int(input("Sua escolha: "))
#     if opcao == 1:
#         adiciona = (input("Qual item você que adiciona a lista: "))
#         lista.append(adiciona)
#     if opcao == 3:
#         print(lista)
#     if opcao == 4:
#         print("Saindo tchau!!!!")
#         break

