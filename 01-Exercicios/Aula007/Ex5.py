#--- Exercício 5 - Funções
#--- Crie uma função para calculo de raiz
#--- A função deve ter uma variável que deternine qual é o indice da raiz(raiz quadrada, raiz cubica...)
#--- Leia um número do console, armazene em uma variável e passe para a função
#--- Realize o calculo da raiz e armazene em uma segunda variável e retorne 
#--- Imprima o resultado e uma mensagem usando f-string, fora da função

numero =  int(input("Insira o número: "))
indice = int(input("Insira o indice: "))

def raiz(num, ind):
    resultado = num ** ind
    return resultado

print(f"A raiz de {numero} elevado a {indice} é: {raiz(numero, indice)}")