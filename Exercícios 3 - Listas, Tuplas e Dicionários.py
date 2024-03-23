#1

'''# lista para guardar as respostas do interrogatório
respostas = []

# lista de perguntas a serem feitas durante o interrogatório
perguntas = [
    "Telefonou para a vítima? ",
    "Esteve no local do crime? ",
    "Mora perto da vítima? ",
    "Devia para a vítima? ",
    "Já trabalhou com a vítima? "
]

# mensagem inicial do interrogatório
print("Interrogatório: \nATENÇÃO: Responda às perguntas com 'sim' ou 'não'.\n")

# loop para fazer cada pergunta e registrar a resposta
for pergunta in perguntas:
    resposta = input(pergunta).lower()  # solicita uma resposta (convertida para minúsculas)
    if resposta == "sim":
        respostas.append(True)  # se a resposta for "sim", adiciona True à lista de respostas
    else:
        respostas.append(False)  # se a resposta for "não" ou outra coisa, adiciona False à lista de respostas

# conta o número de respostas "sim" na lista de respostas
total_sim = respostas.count(True)

#determina a classificação com base no número de respostas "sim"
if total_sim == 2:
    classificacao = "Suspeita"
elif 3 <= total_sim <= 4:
    classificacao = "Cúmplice"
elif total_sim == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"

# imprime a classificação
print("\nClassificação: ", classificacao, "\n")'''



#2

alunos_com_media_acima_ou_igual_a_sete = 0  # inicializa o contador de alunos com média maior ou igual a 7.0

# loop para solicitar informações de cada aluno
for i in range(5):
    nome_aluno = input(f"\nInforme o nome do aluno {i+1}: ")  # solicita o nome do aluno
    notas_aluno = []  # inicializa a lista de notas do aluno
    
    # loop para solicitar as quatro notas do aluno
    for j in range(4):
        nota = float(input(f"Informe a nota {j+1} do aluno {nome_aluno}: "))  # solicita uma nota
        notas_aluno.append(nota)  # adiciona a nota à lista de notas do aluno

    # calcula a média do aluno
    media_aluno = sum(notas_aluno) / len(notas_aluno)
    print(f"\nA média do aluno {nome_aluno} é: {media_aluno}")  # Imprime a média do aluno

    # Verifica se a média do aluno é maior ou igual a 7.0 e atualiza o contador
    if media_aluno >= 7.0:
        alunos_com_media_acima_ou_igual_a_sete += 1

# Imprime o número de alunos com média maior ou igual a 7.0
print(f"\nO número de alunos com média maior ou igual a 7.0 é: {alunos_com_media_acima_ou_igual_a_sete}")



#3

'''carrinho = {'Maça':3.95, 'Uva':5.90, 'Pera':4.99, 'Abacaxi':9.90}

total = sum(carrinho.values())

print(carrinho)
print(f'\nTotal do carrinho: {total:.2f}')'''


#4

'''agenda = {'Lucas': 19191919, 'Laura': 50505050, 'Ange': 12121212, 'Clara':20202020}
print(agenda)

def buscar_contato(agenda, nome):
    #Função para buscar um contato na agenda pelo nome.
    if nome in agenda:
        print(f"Telefone de {nome}: {agenda[nome]}")
    else:
        print(f"O contato {nome} não foi encontrado na agenda.")


# Pedindo ao usuário para procurar um contato
procurar_nome = input("Digite o nome do contato que deseja buscar: ")
buscar_contato(agenda, procurar_nome)
'''

#5

'''#definindo tuplas
tupla_01 = ('01', '02', '03', '04', '05')
tupla_02 = ('a', 'b', 'c', 'd', 'e')

#concatennando as tuplas criadas anteriormente
tupla_03 = (tupla_01 + tupla_02)

print(tupla_03)'''

#6

'''nome = input('Digite seu nome: ')
print(nome.upper()[::-1])'''