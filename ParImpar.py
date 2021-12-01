# Solicitar um número ao usuário
numero = int(input('Digite um número inteiro: '))

# Se o resto da divisão por 2 for igual a zero, o número é par
if (numero%2) == 0:
    print("Par")
else: # Senão o número é ímpar
    print("Ímpar")