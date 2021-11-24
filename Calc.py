# Pede ao usuário o primeiro número e armazena na variável
numero1 = int(input("Entre o primeiro número: "))

# Pede ao usuário o segundo número e armazena na variável
numero2 = int(input("Entre o segundo número: "))
 
# Pede ao usuário o operador matemático e armazena na variável
operador = input("Entre o operador (+ - * /): ")

# Verifica o operador
if operador == '+': # Se for soma, realiza a soma dos números e armazena o resultado na variável
    resultado = numero1 + numero2

if operador == '-': # Se for subtração, realiza a subtração dos números e armazena o resultado na variável
    resultado = numero1 - numero2

if operador == '*': # Se for multiplicação, realiza a multiplicação dos números e armazena o resultado na variável
    resultado = numero1 * numero2

if operador == '/': # Se for divisão, verifica se o segundo número é diferente de zero
    if numero2 != 0: # Se for diferente de zero, realiza a divisão e armazena o resultado na variável
        resultado = numero1 / numero2
    else: # Se não for diferente de zero, exibe mensagem de erro e finaliza a execução
       print("Erro de divisão por zero")
       exit()

print("\n") # Pula uma linha       
print("O resultado da operação é: ", resultado) # Exibe o resultado na tela
print("\n")  # Pula uma linha