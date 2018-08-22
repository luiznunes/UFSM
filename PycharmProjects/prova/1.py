lista_A = []
lista_B = []
lista_C = []

print("Entre com os valores da primeira lista:")
for i in range(10):
    numero = int(input("Entre com o "+str(i+1)+"º número: "))
    lista_A.append(numero)

print("\nEntre com os valores da segunda lista:")
for i in range(10):
    numero = int(input("Entre com o "+str(i+1)+"º número: "))
    lista_B.append(numero)

for num in lista_A:
    if num in lista_B:
        if num not in lista_C:
            lista_C.append(num)

print("\nValores da lista A:")
print(lista_A)
print("\nValores da lista B:")
print(lista_B)
print("\nValores da lista C:")
print(lista_C)