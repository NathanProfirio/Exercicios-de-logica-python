print('os salarios dos funcionarios vai ter um aumento')
print('o aumento dos funcionarios que ganham ate R$1250 vai ser de 15% \nja os funcionario que quanha mais de R$1250 vai se de 10%\n')
print('para saber qual o aumento do seu salario digite seu salario atual abaixo \n=========================')
salario = float(input('salario atual: '))
if salario <= 1250:
   print('o aumento do seu salario sera de {}'.format('15%'))
   print('seu salario novo e: R${:.2f}'.format(salario * 0.15 + salario))
else:
   print('o aumento do seu salario sera de {}'.format('10%'))
   print('seu salario novo e: R${:.2f}'.format(salario * 0.10 + salario))