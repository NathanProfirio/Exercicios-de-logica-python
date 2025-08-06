a = int(input('escreva numeros para saber qual e o maior e o menor numero'))
b = int(input('eccreva numeros para saber qual e o maior e o menor numero'))
c = int(input('escreva numeros para saber qual e o maior e o menor numero'))
#
#teste de qual e o maior numero
if a > b and a > c:
   maior = a
if b > a and b > c:
   maior = b
if c > a and c > b: 
   maior = c
print(maior)

#teste de qual o menor numero
if a < b and a < c:
   menor = a
if b < a and b < c:
   menor = b
if c < a and c < b:
   menor = c
print('o menor numero e o: {} \ne o menor numero e o: {}'.format(menor, maior))