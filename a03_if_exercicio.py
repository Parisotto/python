# Faça uma rotina com o uso de if, elif, else quer receba um valor numérico inteiro entre 1 e 100 e print se a pessoa com a idade obrigatoriamente vota, se vota opcionalmente ou não pode votar
idade = int(input("Digite a idade: "))
# Vota opcional maior de 16 e 60
# Obrigatório maior de 18
if idade >= 60:
    print("O voto é opcional")
elif idade >= 18:
    print("O voto é obrigatório")
elif idade >= 16:
    print("O voto é opcional")
else:
    print("Não pode votar")

if idade >= 60 or idade <=16 and idade >= 16:
    print("O voto é opcional")
elif idade >= 18:
    print("O voto é obrigatório")
else:
    print("Não pode votar")