def multiplicacao():
    mult = 10*2
    file = 'arquivo.txt'

    #ABERTURA DE ARQUIVO

    #abertura para escrita
    arquivo_escrita = open(file, "w")
    arquivo_escrita.write(f'O resultado da multiplicação é: {mult}')
    arquivo_escrita.close()

    #abertura somente para leitura
    arquivo_leitura = open(file, "r")
    leitura = arquivo_leitura.read()
    print(leitura)
    arquivo_leitura.close()

    #abertura de arquivos binários
    '''arquivo_binario = open(file, "wb")'''
    

multiplicacao()