# 1. Faça um programa que determine e mostre os cinco primeiros múltiplos de 3, considerando números
# maiores que 0.

for numero in range(1, 6):
    DivTres = str(numero*3)
    print(f"número 3 x {numero} = {DivTres}")

# 2. Faça um programa que utilize o comando while para mostrar na tela uma contagem regressiva, iniciando
# em 10 e terminando em 0. Mostre também uma mensagem “FIM!” após a contagem

n = 10

while True:
    if n == 0:
        print('Fim!')
        break
    else:
        print(n)
        n -= 1

# 3. Faça um programa que declare um inteiro, inicialize-o com 0, incremente-o de 1000 em 1000, imprimindo
# seu valor na tela, até que seu valor seja 100000 (cem mil).

for numero in range(0, 100001, 1000):
    print(numero)
