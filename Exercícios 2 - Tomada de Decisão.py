#1

'''numero1 = int(input('Digite o número 01: '))
numero2 = int(input('Digite o número 02: '))

if numero1 > numero2:
    print(numero1)
else: 
    print(numero2)'''

#2

'''print('[M]-matutino | [V]-vespertino | [N]-noturno')
turno = input('Escolha seu turno: ')

if turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Boa tarde!')
elif turno == 'N':
    print('Boa noite!')
else:
    print('Valor inválido! Escolha M, V ou N.')'''

#3

'''nota = -1
while nota < 0 or nota > 10:
    nota = int(input('Digite sua nota: '))
    if nota < 0 or nota > 10:
        print('Nota invalida!')
print('Nota inserida com sucesso!')'''

#4

'''nota = -1
while nota < 0 or nota > 10:
    nota = int(input('Digite sua nota: '))
    if nota < 0 or nota > 10:
        print('Nota invalida!')
    elif nota >= 7:
        print('Aprovado')
    else:
        print('Reprovado')'''

#5

'''lado1 = int(input('Digite o valor do lado 01: '))
lado2 = int(input('Digite o valor do lado 02: '))
lado3 = int(input('Digite o valor do lado 03: '))

if lado1 == lado2 & lado1 == lado3 & lado2 == lado3:
    print('Triâgulo Equilátero!')

elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('Triângulo Isósceles')

elif lado1 != lado2 & lado1 != lado3 & lado2 != lado3:
    print('Triângulo Escaleno')'''

#6

'''user = input('Digite seu usuário: ')
senha = input('Digite sua senha: ')

if user != 'admin' or senha != 'admin123':
    print('Usuário ou senha inválido')
else:
    print('Acesso permitido!')'''

#6 (ou)

'''user = input('Digite seu usuário: ')
senha = input('Digite sua senha: ')

if user != 'admin':
    print('Usuário inválido')
elif senha != 'admin123':
    print('Senha inválida')
else:
    print('Acesso permitido!')'''

#7

'''idade = int(input('Digite sua idade: '))

if idade < 10:
    print('Voce á uma criança!')
elif idade > 10 and idade < 18:
    print('Você é um adolescente!')
elif idade > 18 and idade < 60:
    print('Você é um adulto!')
elif idade > 60:
    print('Você é um idoso')'''

#8

'''n1 = float(input('Digite o número 01: '))
n2 = float(input('Digite o número 02: '))
n3 = float(input('Digite o número 03: '))

if n1 > n2 and n1 > n3:
    print(f'{n1} é o maior número')
elif n2 > n1 and n2 > n3:
    print(f'{n2} é o maior número!')
elif n3 > n1 and n3 > n2:
    print(f'{n3} é o maior número!')'''

#9

'''n = -1
impar = 0
par = 0
while n != 0 :
    n = int(input('Digite um número: '))
    resto = n % 2
    if resto == 0 and n != 0:
        par+=1
    elif resto == 1:
        impar+=1

else :
    print('Encerrado')

print(f'{par} número(s) pares e {impar} números ímpares.')'''

#10

'''n1 = int(input('Digite o número 01: '))
n2 = int(input('Digite o número 02: '))
n3 = int(input('Digite o número 03: '))

if n1 > n2 and n1 > n3 and n2 > n3:
    print(f'{n1}, {n2}, {n3}')
elif n1 > n2 and n1 > n3 and n3 > n2:
    print(f'{n1}, {n3}, {n2}')
elif n2 > n1 and n2 > n3 and n1 > n3:
    print(f'{n2}, {n1}, {n3}')
elif n2 > n1 and n2 > n3 and n3 > n1:
    print(f'{n2}, {n3}, {n1}')
elif n3 > n1 and n3 > n2 and n1 > n2:
    print(f'{n3}, {n1}, {n2}')
elif n3 > n1 and n3 > n2 and n2 > n1:
    print(f'{n3}, {n2}, {n1}')'''

#11

'''salario_bruto = float(input('Digite seu salário bruto: '))
salario_liquido = 0

if salario_bruto <= 1903.98:
    print(f'Você é insento do Imposto de Renda. Seu salário líquido é R${salario_bruto:.2f}')
elif salario_bruto > 1903.98 and salario_bruto <= 2826.65:
    salario_liquido = (salario_bruto * 7.5) / 100
    print(f'Seu salário líquido é R${salario_liquido:.2f}')
elif salario_bruto > 2826.65 and salario_bruto <= 3751.05:
    salario_liquido = (salario_bruto * 15) / 100
    print(f'Seu salário líquido é R${salario_liquido:.2f}')
elif salario_bruto > 3751.05 and salario_bruto <= 4664.68:
    salario_liquido = (salario_bruto * 22.5) /100
    print(f'Seu salário líquido é R${salario_liquido:.2f}')
elif salario_bruto > 4664.68:
    salario_liquido = (salario_bruto * 27.5) /100
    print(f'Seu salário líquido é R${salario_liquido:.2f}')'''





