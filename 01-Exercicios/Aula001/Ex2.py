#--- Exercício 2  - Variáveis
#--- Crie um menu para um sistema de cadastro de funcionários
#--- O menu deve ser impresso com a função format()
#--- As opções devem ser variáveis do tipo inteiro
#--- As descrições das opções serão:
#---    Cadastrar funcionário
#---    Listar funcionários
#---    Editar funcionário
#---    Deletar funcionário
#---    Sair
#--- Além das opções o menu deve conter um cabeçalho e um rodapé
#--- Entre o cabeçalho e o menu e entre o menu e o rodapé deverá ter espaçamento de 3 linhas
#--- Deve ser utilizado os caracteres especiais de quebra de linha e de tabulação

opcao = int(input("""
SISTEMA DE CADASTRO DE FUNCIONARIO\n\n\n
    {} - Cadastrar Funcionário
    {} - Listar Funcinários
    {} - Editar Funcionário
    {} - Deletar Funcionário
    {} - Sair\n\n\n
    Escolha uma opção:  """.format(1,2,3,4,5)))

if opcao == 1:
    print("A opção escolhida foi 'Cadastrar funcionário'")
elif opcao == 2:
    print("A opção escolhida foi 'Listar funcionários'")
elif opcao == 3:
    print("A opção escolhida foi 'Editar funcionário'")
elif opcao == 4:
    print("A opção escolhida foi 'Deletar funcionário'")
elif opcao == 5:
    print("A opção escolhida foi 'Sair'")
else:
    pass

