"""
Estruturas condicionais
if, else, elif
"""
idade = 18

if idade < 18:
    print("menor de idade")
elif idade == 18:
    print('você tem exatamente 18 anos')
else:
    print('maior de idade')

"""
Estruturas logicas
And, or, not, is

AND - os dois devem ser verdadeiros
True and False = False
True and True = True
False and False =  False

OR - apenas um precisa ser verdadeiro
True or False = True
True or True = True
False or False = False

Not - inverte
Not True = False
Not False = True

Is - Compara 
exemplo = True
exemplo is True = True
exemplo is False = False
"""

ativo = True
logado = True

if ativo and logado:
    print("está logado")

print(ativo)
print(ativo is False)
print(not ativo)
