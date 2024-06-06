""""
recebendo dados
"""
# Entrada
nome = input("Qual seu nome? \n")

# saída
# 1v
print('Olá {}! Tudo bem?'.format(nome))
# 2v
print('Olá %s, tudo bem?' % nome)
# 3v
print(f'seja bem vindo {nome}')
print(f'você é a {nome + "da silva"}?')