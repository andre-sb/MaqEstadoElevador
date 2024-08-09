from pathlib import Path

from transitions import Machine, State

def v(obj):
    for x in dir(obj):
        if x[0]!='_':
            print(x)



class Elevador:
    direcao=Path('./animacao/direcao.txt')
    tempo=Path('./animacao/tempo.txt')

    def PararMotor(self):
        self.direcao.write_text('0')

    def MotorSubir(self):
        self.direcao.write_text('-1')

    def MotorDescer(self):
        self.direcao.write_text('1')


estados = [
    State('parado'      , on_enter='PararMotor'),
    State('subindo'     , on_enter='MotorSubir'),
    State('descendo'    , on_enter='MotorDescer'),
    ]

transicoes = [
    {'source':'parado',        'trigger':'subir',      'dest':'subindo'        },
    {'source':'parado',        'trigger':'descer',     'dest':'descendo'       },
    {'source':'subindo',       'trigger':'chegou',     'dest':'parado'         },
    {'source':'descendo',      'trigger':'chegou',     'dest':'parado'         },
]

elevador = Elevador()
maquina  = Machine(model=elevador, states=estados, transitions=transicoes, initial='parado')

pass
