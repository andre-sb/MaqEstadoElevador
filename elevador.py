from pathlib import Path

from transitions import Machine

def v(obj):
    for x in dir(obj):
        if x[0]!='_':
            print(x)



class Elevador:
    direcao=Path('./animacao/direcao.txt')
    tempo=Path('./animacao/tempo.txt')



estados = ['parado','subindo','descendo']

transicoes = [
    {'source':'parado',        'trigger':'subir',      'dest':'subindo'        },
    {'source':'parado',        'trigger':'descer',     'dest':'descendo'       },
    {'source':'subindo',       'trigger':'chegou',     'dest':'parado'         },
    {'source':'descendo',      'trigger':'chegou',     'dest':'parado'         },
]

elevador = Elevador()
maquina  = Machine(model=elevador, states=estados, transitions=transicoes, initial='parado')

pass
