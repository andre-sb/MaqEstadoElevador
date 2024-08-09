from pathlib import Path

from transitions import Machine, State, MachineError
from transitions_gui import WebMachine

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
    State('inicio'),
    State('parado'      , on_enter='PararMotor'),
    State('subindo'     , on_enter='MotorSubir'),
    State('descendo'    , on_enter='MotorDescer'),
    ]

transicoes = [
    {'source':'inicio',        'trigger':'iniciar',    'dest':'parado'         },
    {'source':'parado',        'trigger':'subir',      'dest':'subindo'        },
    {'source':'parado',        'trigger':'descer',     'dest':'descendo'       },
    {'source':'subindo',       'trigger':'chegou',     'dest':'parado'         },
    {'source':'descendo',      'trigger':'chegou',     'dest':'parado'         },
]

elevador = Elevador()
maquina  = WebMachine(model=elevador, states=estados, transitions=transicoes, initial='inicio')
elevador.iniciar()

while True:
    comando = input('Evento: ')
    try:
        elevador.trigger(comando)
    except (MachineError, AttributeError):
        print(f'Evento inválido {comando} foi ignorado')
