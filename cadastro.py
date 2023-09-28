def salvarFuncionarios():
    with open("funcionarios.csv", "w") as arquivo:
        for i, funcionario in enumerate(listaFuncionarios, start=1):
            arquivo.write(f"ID: {i}\n")
            arquivo.write(f"Nome: {funcionario['Nome']}\n")
            arquivo.write(f"Setor: {funcionario['Setor']}\n")
            arquivo.write(f"Carga Horária Semanal: {funcionario['Carga Horária Semanal']}\n")
            arquivo.write(f"Salario: {funcionario['Salário']}\n")
            arquivo.write("\n")

def carregarFuncionarios():
    try:
        with open("funcionarios.csv", "r") as arquivo:
            funcionarios = []
            funcionario = {}
            for linha in arquivo:
                linha = linha.strip()
                if linha.startswith("ID:"):
                    if funcionario:
                        funcionarios.append(funcionario)
                        funcionario = {}
                else:
                    # Verifique se a linha contém pelo menos um ':'
                    if ':' in linha:
                        chave, valor = linha.split(": ", 1)
                        funcionario[chave] = valor
            if funcionario:
                funcionarios.append(funcionario)
            return funcionarios
    except FileNotFoundError:
        return []

listaFuncionarios = carregarFuncionarios()

def cadastroFuncionario():
    funcionario = {}
    
    dadoNome = input("Qual o nome do funcionário? ")
    funcionario['Nome'] = dadoNome
    
    dadoSetor = input("Setor: ")
    funcionario['Setor'] = dadoSetor
    
    try:
        dadoCargaHoraria = float(input("Carga Horária Semanal: "))
    except ValueError:
        print("Valor inválido para Carga Horária Semanal. Usando 0.0 como valor padrão.")
        dadoCargaHoraria = 0.0
    funcionario['Carga Horária Semanal'] = dadoCargaHoraria
    
    try:
        dadoSalario = float(input("Salário: "))
    except ValueError:
        print("Valor inválido para Salário. Usando 0.0 como valor padrão.")
        dadoSalario = 0.0
    funcionario['Salário'] = dadoSalario
        
    listaFuncionarios.append(funcionario)
    salvarFuncionarios()
    print("Funcionário cadastrado com sucesso!")

def resumoFuncionario():
    print("Dados da lista de funcionários: ")
    for i, funcionario in enumerate(listaFuncionarios, start=1):
        print(f'ID: {i}, Nome: {funcionario["Nome"]}, Setor: {funcionario["Setor"]}, Carga Horária Semanal: {funcionario["Carga Horária Semanal"]}, Salário: {funcionario["Salário"]}')

def menu():
    print(" - - - - - - - - - MENU - - - - - - - - -")
    print(" | 1 - Cadastrar Funcionário            |")
    print(" | 2 - Resumo de Dados                  |")
    print(" | 3 - Sair                             |")
    print(" - - - - - - - - - - - - - - - - - - - -")
    print("--- Escolha uma opção ---\n")
    op = int(input())
    return op

while True:
    op = menu()
    if op == 1:
        cadastroFuncionario()
    elif op == 2:
        resumoFuncionario()
    elif op == 3:
        print("Saiu")
        break
    else:
        print("Opção inválida, tente novamente.")