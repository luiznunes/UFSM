def retornaMaior(n1, n2, n3):
    maior = n1
    if n2 > maior:
        maior = n2
    if n3 > maior:
        maior = n3

    return maior


n1 = int(input("Entre com o 1º número: "))
n2 = int(input("Entre com o 2º número: "))
n3 = int(input("Entre com o 3º número: "))

maior = retornaMaior(n1, n2, n3)
print(maior)
