# Função de cadastro de nomes e idades
def cadastrar(i_nome, i_idade):
    
    novo_cadastro = []
    novo_cadastro.append(i_nome)
    novo_cadastro.append(i_idade)

    cadastro.append(novo_cadastro)

# Função para exibir o cadastro
def exibir():

    print("\nNomes cadastrados:\n")

    for x in range(len(cadastro)):

        nome = cadastro[x][0]
        idade = cadastro[x][1]
        print("Nome", x+1, ":", nome)
        print("Idade", x+1, ":", idade)

# Função para solicitar as entradas
def solicitar_nomes(qtde):

    for i in range(qtde):
        nome = input("Informe o nome: ")
        idade = int(input("Informe a idade: "))

        cadastrar(nome, idade)

# Rotina principal
cadastro = [] # Declaração do array em branco
quantidade = int(input("Quantos nomes você quer cadastrar? ")) # Pergunta quantos nomes deverão ser cadastrados
solicitar_nomes(quantidade)
exibir()