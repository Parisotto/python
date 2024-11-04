import random

# 0. ADVINHE O NÚMERO
# Escreva um função que faça oo computador escolher um número inteiro entre 1 e 5 e peça ao usuário tentar descobrir qual número foi escolhido pelo computador. O programa deverá escrever no terminal se o usuário acertou ou errou a adivinhação.
def adivinha():
    numero = random.randint(1, 5)
    print("Vou escolher um número entre 1 e 5. Tente adivinhar!")
    adivinha = int(input("Qual número escolhi?: "))
    if adivinha == numero:
        print("Que legal! Você adivinhou")
    else:
        print(f"Xi! Não deu... Eu escolhi {numero}.")

# chama a função adivinha() para executar o jogo
# adivinha()

# 1. CARA OU COROA
# Faça uma função que a pessoa digite c para escolher cara ou k para escolher coroa. Simule o lançamento de uma moeda que resulte em cara (c) ou coroa (k) e diga se a pessoa errou ou acertou na escolha.
def jogar_moeda():
    escolha = ""
    while True:
        # Solicita ao usuário escolher "c" para cara ou "k" para coroa
        escolha = input("Escolha 'c' para cara ou 'k' par coroa: ").lower()
        # Verifica se a escolha é válida
        if escolha not in ['c', 'k']:
            print("Escolha inválida!")
        else:
           break

    # simula o lançamento da moeda
    moeda = random.choice(['c', 'k'])

    # Compara o resultado da moeda com a escolha do usuário
    if moeda == escolha:
        print(f"Parabéns! Você acertou. A moeda resultou em {moeda.upper()}")
    else:
        print(f"Você errou. A moeda resultou em {moeda.upper()}. Sua escolha foi {escolha.upper()}")

# Chama a função para executar o jogo
# jogar_moeda()


# 2. JOGO DE DADOS
# Faça uma função que peça ao usuário escolher um número inteiro de 2 à 12 em seguida simule o lançamento de 2 dados simultaneamente. Compare o resultado da soma dos dois dados com a escolha do usuário e avisar se ele errou ou acertou a jogada. Exemplo: O usuário escolhe 12. Um dado resulta em 6 e o outro também.
def jogar_dados():
    escolha = 0
    while True:
        # Solcita ao usuário escolher um numero inteiro de 2 a 12
        escolha = int(input("Escolha um número inteiro de 2 a 12: "))
        # Verifica se a escolha está dentro do intervalo perimito
        if escolha < 2 or escolha > 12:
            print("Número inválido")
        else:
            break

    # simula o lançamento de dois dados
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    soma_dados = dado1 + dado2
    if soma_dados == escolha:
        print(f"fParabéns! Você acertou. Os dados resultaram em {dado1} e {dado2}, somando {soma_dados}")
    else:
        print(f"Você errou. Os dados resultaram em {soma_dados}")

# Chama a função para executar o jogo
#jogar_dados()

# 3. PAR OU ÍMPAR
# Desenvolva uma função onde o usuário joga par ou impar contra o computador. O usuário digita "par" ou digita "impar" e o programa diz quem ganhou.
def par_ou_impar():
    while True:
        escolha = input("Escolha 'par' ou 'impar': ")
        if escolha not in ['par', 'impar']:
            print("Escolha inválida")
        else:
            break

    numero_usuario = int(input("Escolha um número entre 0 e 5: "))
    numero_computador = random.randint(0, 5)
    soma = numero_computador + numero_usuario
    resultado = "par" if soma % 2 == 0 else "impar"

    print()

# Chama a função para executar o jogo
par_ou_impar()

'''
    S U P E R    D E S A F I O ! ! !
'''

# 4. DOIS OU UM
# Crie uma rotina que recolha o nome de 5 jogadores. O programa deverá sortear 2 ou 1 para cada um dos jogadores. Se um jogador tiver um valor diferente de todos os outros 4 ele deve ser excluído da disputa. A disputa deverá continuar até que restem apenas dois jogadores. Se na rodada nenhum jogador tiver um valor único, a rodada segue sem a retirada de nenhum jogador da disputa. A cada roda deverá ser informado o resultado da disputa e quem foi retirado, se for o caso e uma pausa no programa aguardando dar enter para continuar.

# função usada para criar uma lista com 5 nomes
def recolher_nomes():
    print("Digite seu código aqui. Exclua esta linha")

# função usada para criar um dicionario com os nomes associados a valores aleatórios
def sortear_valores(jogadores):
    print("Digite seu código aqui. Exclua esta linha")

# para verificar se um jogador deve ser excluído da lista se ele foi o único com um valor diferente dos outros 4
def verificar_exclusao(valores):
    print("Digite seu código aqui. Exclua esta linha")

# Função principal que chama as outras funções e executa a parte principal do programa.
def dois_ou_um():
    print("Digite seu código aqui. Exclua esta linha")

# Chama a função para iniciar a disputa
# dois_ou_um()
