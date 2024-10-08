'''
1. Escreva uma função que seja capaz de receber a quantidade de anos e tranformar em meses, dias, horas, minutos e segundos. Saída desejada:
    2 anos equivalem a:
        24 meses
        720 dias
        17280 horas
        1036800 minutos
        62208000 segundos
'''
def calcularTempo(anos):
    meses = anos * 12
    dias = meses * 30
    horas = dias * 24
    minutos = horas * 60
    segundos = minutos * 60

    print(f"{anos} equivalem a:")
    print(f"\t{meses} meses")
    print(f"\t{dias} dias")
    print(f"\t{horas} horas")
    print(f"\t{minutos} minutos")
    print(f"\t{segundos} segundos")

def calcularTempo2(anos):
    print(f"2) {anos} anos equivalem a:")
    print(f"\t{anos * 12} meses")
    print(f"\t{anos * 12 * 30} dias")
    print(f"\t{anos * 12 * 30 * 24} horas")
    print(f"\t{anos * 12 * 30 * 24 * 60} minutos")

def calcularTempo3(anos):
    r = f"{anos} anos equivalem a:\n"
    r += f"\t{anos * 12} meses\n"
    r += f"\t{anos * 12 * 30} dias\n"
    r += f"\t{anos * 12 * 30 * 24} horas\n"
    r += f"\t{anos * 12 * 30 * 24 * 60} horas\n"
    r += f"\t{anos * 12 * 30 * 24 * 60 * 60} horas"
    return r

calcularTempo(2)
calcularTempo2(3)
retorno = calcularTempo3(4)
print(calcularTempo3(4))
