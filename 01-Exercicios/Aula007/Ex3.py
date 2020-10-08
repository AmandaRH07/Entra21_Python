#--- Exercício 3  - Funções
#--- Crie uma função que leia três números float
#--- Armazene cada valor lido em uma variável
#--- Calcule a média entre os três números e armazene em uma quarta variável
#--- Imprima a média e uma mensagem usando f-string (módulo 3)

def media():
    num1 = float(input("Insira o primeiro número: "))
    num2 = float(input("Insira o segundo número: "))
    num3 = float(input("Insira o terceiro número: "))
    media = (num1+ num2 + num3) / 3.0
    print(f"A média entre {num1}, {num2} e {num3} é: {media}")

media()