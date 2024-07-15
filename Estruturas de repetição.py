"""
for valor in entervalo:
    #executa loop
entervalo é o indice de posições dentro de uma váriavel
"Allan Davi" tem 10 entervalos
"A" "L" "L" "A" "N" " " "D" "A" "V" "I"
Valor é o valor da cada dos intevalos
"""

nome = "Allan Davi"
lista = {1, 2, 3, 4}
numero = range(1,10)

"""
for letra in nome:
    print(letra)

for valor in lista:
    print(valor)

for valor in numero:
    print(valor)

# Enumerate -> ((0, "A"),(0, "l"),(0, "l"),(0, "a"),(0, "n")...)
for indice, valor in enumerate(nome):
    print(nome[indice])

for _, valor in enumerate(nome):
    print(valor)
"""

for valor in enumerate(nome):
    print(valor[1], end=";") #0 aparece os indices e 1 aparece os valores, nada aparece os dois

"""

qtd = int(input("informe quantas vezes o loop: "))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'informe o {n}/{qtd} valor: '))
    soma += num
print(soma)
"""
