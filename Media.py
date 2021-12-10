from statistics import mean

# Definição das funções
def solicitar_notas():

    notas = []
    for i in range(4):
        n = int(input("Entre a nota do bimestre: "))
        notas.append(n)
    return notas

def calcular_media(notas):

    m = mean(notas)
    return m

def pular_linha():
    print("\n")

def exibir_notas(n):
    for i in range(len(notas)):
        print("Nota do bimestre", i+1, "=>", notas[i])

def exibir_media(m):
    print("Média: ", m)

def exibe_aprovado(m):
    if (m >= 5):
        print("Resultado: APROVADO")
    else:
        print("Resultado: REPROVADO")

def exibir_resultado(n,m):

    pular_linha() 
    exibir_notas(n)
    pular_linha()
    exibir_media(m)
    exibe_aprovado(m)

# Obtem as notas
notas = solicitar_notas()

# Calcula a média
media = calcular_media(notas)

# Exibe resultados
exibir_resultado(notas, media)























