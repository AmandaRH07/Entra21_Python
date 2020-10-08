# Funções

cabecalho = "SISTEMA DE CADASTRO DE FUNCIONARIO\n\n\n"

rodape = "\n\n\n Obrigada pela preferencia"

def imprimir_tela(conteudo):
    print(cabecalho)
    #print(opcao_menu)
    print(conteudo)
    print(rodape)   

def ler_opcoes():
    opcao = int(input("Insira a opção: "))
    return opcao

def carregar_opcoes(opcao):
    if opcao == 1:
        imprimir_tela("A opção escolhida foi 'Cadastrar funcionário'")
    elif opcao == 2:
        imprimir_tela("A opção escolhida foi 'Listar funcionários'")
    elif opcao == 3:
        imprimir_tela("A opção escolhida foi 'Editar funcionário'")
    elif opcao == 4:
        imprimir_tela("A opção escolhida foi 'Deletar funcionário'")
    elif opcao == 5:
        imprimir_tela("A opção escolhida foi 'Sair'")
    else:
        pass