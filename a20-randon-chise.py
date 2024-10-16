import random

nomes = []
n = 5
while len(nomes) < n:
    resp = input(f"Digte {len(nomes) + 1}° nome: ")
    nomes.append(resp)
    # print(nomes)

nomeSorteado = random.choice(nomes)
#print(f"{nomeSorteado} foi o nome sorteado!")
sair = "n"
while sair != "s":
    random.shuffle(nomes)
    print(nomes)
    sair = input("Sair ditite s: ")
