antecessor seu sucessor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

numero = int (input('digite um numero para saber seu antecessor e seu sucessor:'))
antes = (numero - 1)
depois = (numero + 1)
print('O numero que voce escolheu e o {} seu antecesso e {} e seu sucessor e {}'.format(numero, antes, depois))

=======================================================================================================================================================================
dobro e tripo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

n = int (input('escolha um numero:'))
a = n * 2
b = n * 3
c = float( n ** (1/2))
print('o dobro do seu numero e: {} \n o tripo e: {} \n a raiz quadrada e: {}'.format(a, b, c)) 

=======================================================================================================================================================================
calculo de media de duas notas
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

primeira = float(input('qual sua primeira nota:'))
segunda = float(input('qual sua segunda nota:'))
media = float((primeira + segunda)/2)
print ('sua media e ',media)

=======================================================================================================================================================================
conversor de metros para centrimetros e milimitros
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

metros = float (input ('digite um numero em metros ele sera convertido em centimetros e milimitros'))
c, m = ((metros * 100, metros * 1000))
print('centimetos: {} \n milimetros: {} '.format(c, m))

=======================================================================================================================================================================
tabuada 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

n = int(input('escreva um numero para ver a tabuada desse numero: '))
a, b, c, d, e, f ,g ,h ,i = (n * 1, n * 2, n * 3, n * 4, n * 5, n * 6, n * 7, n * 8, n * 9)
print('=' * 18)
print('A tabuada do ',n)
print('{}x{} = {} '.format(n, '1', a))
print('{}x{} = {} '.format(n, '2', b))
print('{}x{} = {} '.format(n, '3', c))
print('{}x{} = {} '.format(n, '4', d))
print('{}x{} = {} '.format(n, '5', e))
print('{}x{} = {} '.format(n, '6', f))
print('{}x{} = {} '.format(n, '7', g))
print('{}x{} = {} '.format(n, '8', h))
print('{}x{} = {} '.format(n, '9', i))

=======================================================================================================================================================================
convesor de real em dolar
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

print('=' * 18)
real = float (input('Digite quantos reais voce tem na carteira para saber quantos dolas voce pode compra R$'))
dolar = float(input("DIgite o valor do dolar hoje: ")
resultado = (real / dolar)
print('seu dinheiro convertido en dolares e ${:.2f}'.format(resultado))

=======================================================================================================================================================================
calculadora de gasto de latas de tintas para pinta uma parede
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

print('para saber quanto de tinta voce vai gasta para pinta uma parede digite a largura e altura da parede')
largura = float(input('Qual a largura das parede? '))
altura = float(input('Qual a altura da parede? '))
area = float(largura * altura)
tinta = int( (area / 2))
print('voce vai gasta {} latas de tinta'.format(tinta))

=======================================================================================================================================================================
calculadora de desconto
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

preço = float(input('digite o valor do produto sem desconto: '))
desconto = int(input('digite quantos porcentos de desconto sera aplicado no produto: '))
convesao = (desconto/100)
valor = (preço - preço * convesao)
print('o preço do produto com {}{} sera: {:.2f} '.format(desconto,'%', valor))

=======================================================================================================================================================================
calculo de aumento de salario
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

salario = float (input('digite seu salario: atual: '))
aumento = int (input('o seu salario sera aumentado em quantos porcentos? '))
convesao = (aumento/100)
novo =  (salario + convesao * salario)
print('seu novo salario com o aumento de {}{} sera no valor de: R${:.2f}'.format(aumento, '%', novo))

