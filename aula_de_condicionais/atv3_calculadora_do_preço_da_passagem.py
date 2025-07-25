print('o valor da passagem e cobrado da seguinte forma ')
print('50 centavos por KM de distancia do ponto de embargue ate o ponto de desembarque para viagens de ate 200KM de distancia')
print('para viagens acima de 200 KM o valor e de 45 centavos por diatancia do ponto de embargue ate o ponto de desembarque')
distancia = (float(input('digite a distancia da viagem em KM para saber o valor da passagem: ')))
if distancia <= 200:
   print('o valor da sua passagem sera de R$ {:.2f} reais'.format(distancia * 0.50))
else:
   print('o valor da sua passagem sera de R$ {:.2f} reais'.format(distancia * 0.45))
