#  1. Faça um programa que receba dois números inteiros e mostre qual deles é o maior.
"""
compara = int(input("informe um número: ")), int(input("informe um número: "))

if compara[0] > compara[1]:
    print(compara[0])
else:
    print(compara[1])
"""
#  2. Faça um programa que leia um número inteiro fornecido pelo usuário. Se esse número for positivo, calcule
# a raiz quadrada do número e apresente-a. Se o número for negativo, mostre uma mensagem dizendo que o
# número é inválido
"""
from math import sqrt

num = int(input("informe um número: "))

if num > 0:
    print(sqrt(num))
else:
    print("número invalido")
"""
# 3. Faça um programa que recebe um número inteiro e informe se este número é par ou ímpar.

num = int(input("informe um número: "))

if num % 2 == 0:
    print('par')
else:
    print('impar')
