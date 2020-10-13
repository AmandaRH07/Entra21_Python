# Arquivos - Manipulação Texto

#== Open

#== Escrita
#-- x = cria um novo arquivo, caso o arquivo já exista, dá erro
#-- w = cria um novo arquivo, porem se o arquivo jé existir, apaga o antigo
#-- a = adiciona uma linha no final do aquivo
dict_person = {'first': "Amanda", 'last': 'Hass'}
arquivo = open('pessoa.txt','a')
arquivo.write(f"{dict_person['first']};{dict_person['last']}\n")
arquivo.close()

#== Leitura
arquivo = open("pessoa.txt", 'r')
for linha in arquivo:
    linha_limpa = linha.strip() #tira caracteres especiais
    lista_dados = linha_limpa.split(';')
    print(f"nome:{lista_dados[0]} - sobrenome: {lista_dados[1]}")
arquivo.close()