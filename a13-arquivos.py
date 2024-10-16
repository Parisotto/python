# Manipulando arquivos texo
import os

# CRIANDO E ESCREVENDO ARQUIVOS TEXTO
with open('arquivo.txt', 'w') as arquivo:
    arquivo.write("Ola, mundo!\n")
    arquivo.write("Estou aqui!\n")
    linhas = ['Brasil\n', 'Argentina\n','Italia']
    arquivo.writelines(linhas)

texto = "Aqui vai uma mensagem"
with open('outro-arquivo.txt', 'w') as arquivo:
    arquivo.write(texto)

arquivo = open('mais-um-arquivo.txt', 'w')
arquivo.write(texto + "\n")
arquivo.write("Outra linha" + "\n")
arquivo.write("Finalizei o texto" + "\n")
arquivo.close()

# ABRINDO E LENDO ARQUIVOS
with open("arquivo.txt", 'r') as arquivo:
    for linha in arquivo:
        print(linha)

lista = []
with open('arquivo.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    print(linhas)
    for linha in linhas:
        lista.append(linha)
    print(linhas)

os.rename('arquivo.txt', 'excluir.txt')
os.remove('excluir.txt')
