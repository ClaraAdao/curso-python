# o que são listas

lista_frutas = [] #declaração da lista
fruta = input("Digite uma fruta: ")
lista_frutas.append(fruta)
lista_frutas.append('Maçã')
lista_frutas.append('Uva')
lista_frutas.append('Banana')
print(lista_frutas)

#tupla

tupla = ('Maçã', 'Banana', 'Uva', 'Morango')
print(tupla)

    # OBS: print(lista_frutas[-1]) - retorna o último item da lista no caso 'Banana'


    #diferença entre lista e tupla é que na tupla o valor não pode ser alterado e todos valores devem ser do mesmo tipo

#dicionários

dicionario = {}
dicionario['maça'] = 'É uma fruta'
dicionario['carro'] = 'É um veículo'
dicionario['gato'] = 'É um animal'
print(dicionario)
