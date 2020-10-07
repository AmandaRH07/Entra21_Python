#--- Exercício 3  - Variáveis
#--- Imprima dois parágrafos do último livro que você leu
#--- A impressão deve conter informações do livro, que deverão estar em variáveis
#--- As informações do Livro serão: 
#---    Título
#---    Edição
#---    Autor
#---    Data de publicação
#--- Os parágrafos devem estar formatados conforme a formatação do livro

titulo = "A Revolução dos Bichos"
edicao = "1ª edição"
autor = "George Orwel"
publicacao = "17/08/1945"

print("Título: {}".format(titulo))
print("Edição: {}".format(edicao))
print("Autor: {}".format(autor))
print("Data de publicação:  {}".format(publicacao))

print(f"""
    Realmente, era uma discussão violenta. Gritos, socos na mesa, olhares suspeitos, furiosas negativas. A 
origem do caso, ao que parecia, fora o fato de Napoleão e o Sr. Pilkington haverem, ao mesmo tempo, jogado 
um ás de espadas.\n
    Doze vozes gritavam cheias de ódio e eram todas iguais. Não havia dúvida, agora, quanto ao que sucedera 
à fisionomia dos porcos. As criaturas de fora olhavam de um porco para um homem, de um homem para um porco e 
de um porco para um homem outra vez; mas já se tornara impossível distinguir quem era homem, quem era porco.""")


