# Usando TRY ... EXCEPT

def dividir(a, b):
    if b != 0:
        quociente = a / b
        print(f"{a} dividido por {b} é {quociente}")
    else:
        print(f"Ipossível divir por 0 (zero!)")

a = int(input("SEM TRY - Digite o dividendo: "))
b = int(input("SEM TRY - Digite o divisor: "))
dividir(a, b)

def dividirComTry():
    try:
        dividendo = int(input("COM TRY - Digite o dividendo: "))
        divisor = int(input("COM TRY - Digite o divisor: "))
        quociente = dividendo / divisor
        print(f"{dividendo} dividido por {divisor} é igual a {quociente}")
    except ValueError:
        print(f"ERRO!: Você digitou um valor inválido")
    except ZeroDivisionError:
        print(f"Impossível dividir por 0 (zero)!")
    else:
        print("Nenhum erro ocorreu!")
    finally:
        print("Este bloco 'finally' sempre será executado")

dividirComTry()
