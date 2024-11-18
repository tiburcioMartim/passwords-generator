import random, string, csv, os

def gerar_senha(tamanho, usar_maiusculo, usar_numeros, usar_especiais):
    caracteres = string.ascii_lowercase
    if usar_maiusculo:
        caracteres += string.ascii_uppercase
    if usar_numeros:
        caracteres += string.digits
    if usar_especiais:
        caracteres += string.punctuation
    
    senha = "".join(random.choice(caracteres) for i in range(tamanho))
    return senha

tamanho = int(input("Qual será o tamanho da senha? "))
usar_maiusculo = input("Incluir letras maiusculas? (s/n)").lower() == "s"
usar_numeros = input("Incluir números? (s/n)").lower() == "s"
usar_especiais = input("Incluir caracteres especiais? (s/n)").lower() == "s"

senha = gerar_senha(tamanho, usar_maiusculo, usar_numeros, usar_especiais)

if os.path.exists("log.csv"):
    with open("log.csv", "r", newline="") as csvfile:
        reader = csv.reader(csvfile)
        index = sum(1 for row in reader) + 1
else:
    index = 0

with open("log.csv", "a", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([index, senha])

print(f"Sua senha gerada é: {senha}")