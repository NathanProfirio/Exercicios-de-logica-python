print('para saber se nosso banco libera o financiamento da casa para voce digite as informações abaixo:')
casa = float(input('o valor da casa: '))
salario = float(input('seu salario mensal: '))
anos = int(input('em quantos anos voce quer parcela a casa: '))
meses = (anos * 12)
parcela = float(casa / meses)
if parcela <= salario - salario * 0.30:
   input('seu financiamento foi aceito \nsuas parcelas serão de R${:.2f} \ndurante {} meses '.format(parcela, meses))
else:
   print('seu financiamento foi negado')