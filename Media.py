# Obtem as notas
nota1 = int(input("Entre a nota do primeiro bimestre (0-10): "))
nota2 = int(input("Entre a nota do segundo bimestre (0-10): "))
nota3 = int(input("Entre a nota do terceiro bimestre (0-10): "))
nota4 = int(input("Entre a nota do quarto bimestre (0-10): "))

# Calcula a média
media = ( nota1 + nota2 + nota3 + nota4 ) / 4

# Exibe as notas e a média
print("\n") 
print("Nota do primeiro bimestre: ", nota1)
print("Nota do segundo bimestre: ", nota2)
print("Nota do terceiro bimestre: ", nota3)
print("Nota do quarto bimestre: ", nota4)
print("\n")
print("Média: ", media)

# Exibe o resultado aprovado ou reprovado
if (media >= 5):
    print("Resultado: APROVADO")
else:
    print("Resultado: REPROVADO")




















