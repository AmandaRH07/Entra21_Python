# Funções

# ligar arquivos
from Aula007_2 import imprimir_tela, ler_opcoes, carregar_opcoes

opcao_menu = """
    {} - Cadastrar Funcionário
    {} - Listar Funcinários
    {} - Editar Funcionário
    {} - Deletar Funcionário
    {} - Sair""".format(1,2,3,4,5)

imprimir_tela(opcao_menu)
item = ler_opcoes()
carregar_opcoes(item)