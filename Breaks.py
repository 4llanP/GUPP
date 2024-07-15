"""
Utilizamos o break para sair de loops de maneira planejada

"""

for numero in range(1, 11):
    if numero == 15:
        break
    else:
        print(numero)
print("fora do loop")


while True:
    comando = input("Sair? ")
    if comando == "sim":
        break
