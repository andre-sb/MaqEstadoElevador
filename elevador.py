from pathlib import Path

def v(obj):
    for x in dir(obj):
        if x[0]!='_':
            print(x)

class Elevador:
    direcao=Path('./animacao/direcao.txt')
    tempo=Path('./animacao/tempo.txt')

pass