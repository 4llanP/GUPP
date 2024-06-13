""""
Numérico = númericos inteiros
"""
print("="*5, 'Num', '='*5)

num = 1_000_000

print(num)

print('='*50)

"""
Float - númericos fracionados
"""
print("="*5, 'Float', '='*5)
quebrado = 5.6
diferenca = int(quebrado)
print(quebrado+quebrado)
print(diferenca+diferenca)
# Entende como int e ignora após o .
print('='*50)
"""
Boleana - verdadeira ou falso

True e False
não
true e false
"""
print("="*5, 'Bool', '='*5)
ativo = True
print(ativo)
print(not ativo)
print('='*50)
"""
String
Tudo que estiver dentro de aspas simples, duplas ou triplas
"""
print("="*5, 'String', '='*5)
nome = 'Allan'
print(nome)

nome = 'allan davi bernardes puga tavares'
print(nome.capitalize())
print(nome.title())
print(nome.upper())

texto = """Exemplo de pulo
o texto mantem a formatação dentro das triplas"""
print(texto)

# [0, 1, 2, 3, 4]
# [a, l, l, a, n]
nome = 'allan davi'
print(nome[1:3])
print(nome.split()[1])
print(nome[4::-1])
print(nome[0::2])

print('='*50)
