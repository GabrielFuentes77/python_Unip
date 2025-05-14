import json

with open("Dados.Json", "r") as arquivos:
    lista_Carregada = json.load(arquivos)

print(lista_Carregada)

print(lista_Carregada[0]["email"])