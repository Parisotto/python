# TUPLA
# tupla = (elemento1, elemnto2, ...)

variavel1 = 9 # variável tipo numérica
variavel2 = "Texto" # variável tipo string
variavel3 = True # variável do tipo boleano
variavel4 = ["item1", "item2", "item3"] # lista
variavel5 = ("item1", "item2", "...") # tupla
variavel6 = {1,2,3,4,...} # set ou conjunto

tupla = (1, "Olá", 3.14, True, 'c') # é imutável
tuplaDireta = 0, "Edson", 1.618, 'p', "Edson"
tuplaVazia = ()
tuplaSimples = (27,)

print(tupla[1])
print(tupla[3])

print()
for indice, elemento in enumerate(tupla):
    print(f"{indice}: {elemento}")

tuplaAninhada = ((1,2,3), 9, True,[1,4,"sim"])
print()
print(tuplaAninhada[0])
print(tuplaAninhada[1])
print(tuplaAninhada[3][2])

print(len(tuplaDireta))
print(tupla.index(3.14))
print(tuplaDireta.count("Edson"))

string = "Curso de Python"
print(tuple(string))

novaTupla = tuple(string)
print(novaTupla)

