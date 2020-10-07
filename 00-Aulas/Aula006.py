# Dicionários

#== declaração vazio
dicionario_pessoa1 = {}

#== declaração com chave/valor
dicionario_pessoa2 = {'nome': 'Arthur'}

#== adicionando chave após a criação do dicionario
dicionario_pessoa1['nome'] = 'Helion'
dicionario_pessoa1['idade'] = 32

dicionario_pessoa2['idade'] = 27

#== alterando o valor de uma chave
dicionario_pessoa2['idade'] = 17
dicionario_pessoa2['end'] = 'rua...'
dicionario_pessoa2['bairro'] = 'centro...'

#== removendo uma chave do dicionário
del dicionario_pessoa2['end']
bairro = dicionario_pessoa2.pop('bairro')

#== CRUD => Create, Read, Update, Delete

print(dicionario_pessoa1['nome'], dicionario_pessoa1['idade'])

#== Lendo dados de forma dinamica
for chaves, valor in dicionario_pessoa2.items():
    print(chaves, '-', valor)
    if chaves == 'idade' and valor < 18:
        dicionario_pessoa2['idade'] = 18


#print(dicionario_pessoa1)
print(dicionario_pessoa2)