# DICIONÁRIO
# dicionario = {chave:valor}
# dicionario = dict(chave:valor)

dicionario = {}

dicionario["Cidade"] = "São Paulo"
dicionario["Estado"] = "SP"
dicionario["Região"] = "Sudeste"

print(dicionario)
print(dicionario["Cidade"])
print(dicionario.get("Estado"))
print(dicionario.get("ChaveInexistente"))
print(dicionario.get("ChaveInexistente", "Valor alternativo se chave não existir"))

frutas = {
    "Laranja: R$5,00",
    "Pera: R$3,00"
}
#print(frutas)
