salario = float (input('digite seu salario: atual: '))
aumento = int (input('o seu salario sera aumentado em quantos porcentos? '))
convesao = (aumento/100)
novo =  (salario + convesao * salario)
print('seu novo salario com o aumento de {}{} sera no valor de: R${:.2f}'.format(aumento, '%', novo))

