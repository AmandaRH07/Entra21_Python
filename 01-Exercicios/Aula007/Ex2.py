#--- Exercício 2  - Funções
#--- Escreva uma função que leia dois números do console
#--- Armazene cada número em uma variável
#--- Realize a divisão entre os dois números e armazene o resultado em uma terceira variável
#--- Imprima o resultado e uma mensagem usando f-string

def divisao(num1, num2):
    if num2 == 0:
        print("Operação inválida. O divisor não pode ser 0")
    else:
        resultado = num1/num2
        return resultado

numero1 = int(input("Insira o número1: "))
numero2 = int(input("Insira o número2: "))

print(f"A divisão entre {numero1} e {numero2} é {divisao(numero1,numero2)}")