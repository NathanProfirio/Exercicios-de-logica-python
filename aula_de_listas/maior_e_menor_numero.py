numeros = []
maior_numero = 0
posicao_do_maior = ""
menor_numero = 0
posicao_do_menor = ""

for l in range(0, 5):
    numeros.append(int(input("escreva um numero: ")))
    if l == 0:
        maior_numero = numeros[0]
        menor_numero = numeros[0]

    if numeros[l] >= maior_numero:
        maior_numero = numeros[l]

    if numeros[l] <= menor_numero:
        menor_numero = numeros[l]
       
for p, n in enumerate(numeros):
    if n == maior_numero:
        posicao_do_maior += str(f"{p}, ")
    if n == menor_numero:
        posicao_do_menor += str(f"{p}, ")

print(f"Os numeros digitados foram {numeros}")
print(f"O maior numero digitado foi o {maior_numero} nas posições {posicao_do_maior}")
print(f"O menor numero digitado foi o {menor_numero} nas posições {posicao_do_menor}")