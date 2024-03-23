#1

'''def soma(a,b,c):
    calculo = a+b+c
    print(f'Resultado: {calculo}')

print('Digite os valors que deseja somar: \n')
a = int(input('Número 01: '))
b = int(input('Número 02: '))
c = int(input('Número 03: '))

soma(a,b,c)'''

#2

'''def inverter_int(numero):
    numero = str(numero)
    print(f'Número invertido: {numero[::-1]}')

numero = int(input('Digite um número: '))
inverter_int(numero)'''

#3

'''def celsius_para_fahrenheit(temperatura):
    conversao = (temperatura * 9/5) + 32
    print(f'A temperatura em Fahrenheit é: {conversao:.2f}')

def fahrenheit_para_celsius(temperatura):
    conversao = (temperatura - 32) * 5/9
    print(f'A temperatura em Celsius é: {conversao:.2f}')

def menu():
    opcao = int(input('Qual conversão deseja realizar? \n(1) Celsius -> Fahrenheit \n(2) Fahrenheit -> Celsius \n\nDigite (1) ou (2): '))

    if opcao == 1:
        print('\nVocê escolheu Celsius -> Fahrenheit')
        temperatura = float(input("Digite a temperatura: "))
        celsius_para_fahrenheit(temperatura)
    elif opcao == 2:
        print('\nVocê escolheu Fahrenheit -> Celsius')
        temperatura = float(input("Digite a temperatura: "))
        fahrenheit_para_celsius(temperatura)
    else:
        print('Opção Inválida. Tente novamente: \n')
        menu()

menu()'''

#4

'''def dolar_americano(real):
    conversao = real / 4.91
    print(f'{conversao:.2f} dólares americano')

def peso_argentino(real):
    conversao = real / 0.02
    print(f'{conversao:.2f} pesos argentinos')

def dolar_australiano(real):
    conversao = real / 3.18
    print(f'{conversao:.2f} dólares australiano')

def dolar_canadense(real):
    conversao = real / 3.64
    print(f'{conversao:.2f} dólares canadense')

def franco_suico(real):
    conversao = real / 0.42
    print(f'{conversao:.2f} francos suiço')

def euro(real):
    conversao = real / 5.36
    print(f'{conversao:.2f} euros')

def libra_esterlina(real):
    conversao = real / 6.21
    print(f'{conversao:.2f} libras esterlina')

print('CALCULAR CÂMBIO\n')

real = float(input('Digite quantos reais voce tem: R$'))

print(f'\nCom R${real} você poderia comprar: \n')

dolar_americano(real)
peso_argentino(real)
dolar_australiano(real)
dolar_canadense(real)
franco_suico(real)
euro(real)
libra_esterlina(real)'''

#5 

'''def contar_vogais(texto):
    total = 0
    for i in texto:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            total+=1
    print(f'Total de vogais: {total}')

texto = input('Digite seu texto: ')
contar_vogais(texto)'''

#6

'''import random

def jogo_da_forca(chances):
    while True:
        for letra in palavra:
            if letra.lower() in letras_usuario:
                print(letra, end=" ")
            else:
                print("_", end=" ")
            
        print(f'Você tem {chances} chances')

        tentativa = input('Adivinhe uma letra: ')
        letras_usuario.append(tentativa.lower())

        if tentativa.lower() not in palavra.lower():
            chances-=1

                    
        ganhou = True

        for letra in palavra:
            if letra.lower() not in letras_usuario:
                ganhou = False
        if chances == 0 or ganhou:
            break

    if ganhou:
        print(f'Parabéns, você ganhou! :) \nA palavra era: {palavra}')
    else:
        print(f'Você perdeu! :( \nA palavra era: {palavra}')

lista = ['bagunça', 'texto', 'amor', 'missão', 'abacate', 'almoxarifado', 'lasanha', 'mingual', 'americana', 'argentina']

palavra = random.choice(lista)

letras_usuario = []
chances = 6
ganhou = False

jogo_da_forca(chances)'''