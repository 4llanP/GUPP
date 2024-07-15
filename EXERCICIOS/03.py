#  1. Faça um programa que leia um número inteiro e imprima-o.

# print(input("informe um número: "))

#  2. Faça um programa que peça para o usuário digitar três valores inteiro e imprima a soma deles.
# print(int(input("informe 3 números para serem somados: ")) + int(input("informe 3 números para serem somados: ")) +
#      int(input("informe 3 números para serem somados: ")))

#  3. Faça um programa que recebe três valores e apresente a soma dos quadrados dos valores lidos.


def eleva2(valor):
    valor = valor ** 2
    return valor


soma = 0

for numero in range(1, 4):
    soma += eleva2(int(input("Informe o valor:")))
#    print(soma)
print(soma)
