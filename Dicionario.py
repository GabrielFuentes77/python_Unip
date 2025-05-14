import json
#Parte 2: Dicionarios

cont = 0
lista = []
n = int(input("Quantos usuários deseja cadastrar? "))

while (cont < n):
    agenda = {}
    agenda["nome"] = input("Nome: ")
    agenda["celular"] = input("Celular: ")
    agenda["email"] = input("E-mail: ").lower()
    lista.append(agenda)
    cont += 1
    print("")


with open("dados.json","w") as arquivos:
    json.dump(lista,arquivos,indent=4)