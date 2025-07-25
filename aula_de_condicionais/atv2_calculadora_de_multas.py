print('A velocidade maxima permitida nessa avenida e 80 Km/H e a multa e R$ 7.00 reias por KM/H acima dessa velocidade')
velocidade = float(input('para saber se seu carro foi multado e o valor da multa digite a velocidade do carro em KM/H: '))
if velocidade <= 80:
   print('voce não foi multado')
else:
   multa = ((velocidade - 80) * 7.00)
   print('voce estava a cima da velocidade permitida na avenida foi multado no valor de: R$ {} Reais'.format(multa))
