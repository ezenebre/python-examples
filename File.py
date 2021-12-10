# Abrir e ler 
f = open("demofile.txt")
print(f.read())

# Gravar 
with open("test.txt", 'w', encoding = 'utf-8') as w:
    w.write("Hello World")