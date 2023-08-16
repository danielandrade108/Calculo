from math import pow, floor, ceil

nome = str(input('Bem vindo! Informe seu nome: '))
print('Ola', nome, '! Pronto para descobrir seu IMC?')

peso = float(input('Quanto você pesa em Kg? (kg) '))
altura = float(input('Quanto você mede em altura? (m)'))
IMC = peso/(altura**2)

print('Seu IMC é', IMC)

if IMC < 18.5:
    print('Vocẽ está abaixo do peso em. É melhor comer um pouquinho mais.')
elif 18.5 <= IMC <25:
    print('Parabéns, o seu peso está normal!! Continue assim!!')
elif 25 <= IMC <30:
    print('Diagnóstico: sobrepeso')
elif 30 <= IMC <40:
    print('Diagnóstico: obeso')
elif IMC >=40:
    print('Diagnóstico: obesidade mórbida')