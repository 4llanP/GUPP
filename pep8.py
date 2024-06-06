""""
PeP 8 - Proposta para escrita de códigos em python

[1]- CamelCase para criação de classes;

Class CalculadoraCientifica:

[2]- Variaveis e funções separar com underline e começar com minusculo;

Def soma_dois
numero_impar

[3]- 4 espaços para identação!

if "a" in "banana":
    print('tem')

[4]- Linhas em branco

class TipoTananm:
    pass


class TipoBananam:
    pass

[5]- imports em linhas separadas

Errado
import sys, os

Certo
import sys
import os

diferente quando não é o pacote completo

from types import StringType, ListType

Tendo vários pode usar a configuração

from types import (
    StringType,
    ListType,
    setType
)

6 - Sem espassos em expressões e funções
errado
funcao(      algo[ 1 ], {outro: 2      }    )
certo
funcao(algop[1],{outro:2})

[7]- termine instrução com uma nova linha
exemplo abaixo, deixa uma linha em brnaco no fim do código
"""
