# Arquivos - Manipulação Texto

#== Open

#== Escrita
#-- x = cria um novo arquivo, caso o arquivo já exista, dá erro
#-- w = cria um novo arquivo, porem se o arquivo jé existir, apaga o antigo
#-- a = adiciona uma linha no final do aquivo
dict_person = {'first':"Amanda", 'last':'Hass', 'age':18}
arquivo = open('pessoa.txt','a')
arquivo.write(f"{dict_person['first']};{dict_person['last']};{dict_person['age']}; \n")
arquivo.close()

#== Leitura
arquivo = open("pessoa.txt", 'r')
for linha in arquivo:
    linha_limpa = linha.strip() #-- limpa espaços em brando e caracteres de formatação (\n \t)
    lista_dados = linha_limpa.split(';')
    print(f"nome:{lista_dados[0]} - sobrenome:{lista_dados[1]}, idade:{lista_dados[2]}")

arquivo.close()