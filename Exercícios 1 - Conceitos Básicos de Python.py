# 1

'''
numero1 = int(input('Digite o número 1: '))
numero2 = int(input('Digite o número 2: '))
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

print(f'Soma = {soma} \nSubtração = {subtracao} \nMultiplicação = {multiplicacao} \nDivisão = {divisao}')

'''

# 2

'''

nascimento = int(input('Digite o ano do seu nascimento: '))
idade = 2024 - nascimento
print(f'Você tem {idade} anos')

'''

# 3

'''

km = int(input('Digite a distância em quilômetros: '))
metros = km*1000
centimetros = km*100000
milimetros = km*1000000
print(f'{km}km é igual a: \n{metros}m \n{centimetros}cm \n{milimetros}mm')

'''

# 4

'''
qtd_litros = int(input('Olá, diga a quantidade de combustível consumido em litros: '))
distancia = int(input('Agora digite a distância percorrida em km: '))
consumo = distancia // qtd_litros
print(f'O consumo médio foi de {consumo}km/l')

'''

#5

'''
distancia = float(input("Digite a distância em km:"))
tempoA = distancia / 600
tempoC = distancia / 100
tempoO = distancia / 80

tempoA_s = int(tempoA * 3600)  # convertemos de horas para segundos
horasA = int(tempoA_s / 3600)  # parte inteira
tempoA_s = int(tempoA_s % 3600)  # o resto
minutosA = int(tempoA_s / 60)
segundosA = int(tempoA_s % 60)

tempoC_s = int(tempoC * 3600)  # convertemos de horas para segundos
horasC = int(tempoC_s / 3600)  # parte inteira
tempoC_s = int(tempoC_s % 3600)  # o resto
minutosC = int(tempoC_s / 60)
segundosC = int(tempoC_s % 60)

tempoO_s = int(tempoO * 3600)  # convertemos de horas para segundos
horasO = int(tempoO_s / 3600)  # parte inteira
tempoO_s = int(tempoO_s % 3600)  # o resto
minutosO = int(tempoO_s / 60)
segundosO = int(tempoO_s % 60)

print(f'O tempo estimado para sua viagem de Avião é de: {horasA}h {minutosA}m {segundosA}s')
print(f'O tempo estimado para sua viagem de Carro é de: {horasC}h {minutosC}m {segundosC}s')
print(f'O tempo estimado para sua viagem de Ônibus é de: {horasO}h {minutosO}m {segundosO}s')



#print("O tempo estimado é de %5.2f horas" % tempo)

# Opcional: imprimir o tempo em horas, minutos e segundos

tempo_s = int(tempo * 3600)  # convertemos de horas para segundos
horas = int(tempo_s / 3600)  # parte inteira
tempo_s = int(tempo_s % 3600)  # o resto
minutos = int(tempo_s / 60)
segundos = int(tempo_s % 60)
print("%05d:%02d:%02d" % (horas, minutos, segundos))

'''

# 6

'''

peso = float(input('Informe seu peso e kg: '))
altura = float(input('Informe sua altura em metros: '))
imc = peso / (altura*altura)
print(f'Seu Índice de Massa Corporal é: {imc:.2f}')

'''

# 7

'''
s_hora = float(input('Informe quanto você recebe por hora: '))
h_mes = float(input('Informe quantas horas você trabalhou nesse mês: '))
s_mes = s_hora * h_mes
print(f'Seu salário no final desse mês será de R${s_mes:.2f}')

'''

# 8

'''
horas = float(input('Informe quantas horas de exercício físico você faz por semana: '))
segundos = int(horas * 3600)
minutos = int(segundos / 60)
calorias = int(minutos * 5)
print(f'Você perdeu aproximadamente: {calorias}kcal')

'''

# 9

'''
nome = input("Nome: ")
sobrenome = input('Sobrenome: ')
nascimento = int(input('Ano em que nasceu: '))
cidade = input('Cidade que deseja visitar: ')
idade = 2024 - nascimento

print(f'Olá, {nome} {sobrenome}! {cidade} é um lugar incrível para visitar com {idade} anos.')

#español

nombre = input("Nombre: ")
apellido = input('Apellido: ')
nascimiento = int(input('Año en que nasciste: '))
ciudad = input('Cuál ciudad tienes ganas de conocer?: ')
edad = 2024 - nascimiento

print(f'Hola {nombre} {apellido}! {ciudad} es un sítio increíble para conocer con {edad} años.')

'''