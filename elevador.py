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
        self.tempo.write_text('0.2')        

    def MotorSubir(self):
        self.direcao.write_text('-1')
        self.tempo.write_text('0.2')

    def MotorDescer(self):
        self.direcao.write_text('1')
        self.tempo.write_text('0.2')

    def MotorAceleraSobe(self):
        self.direcao.write_text('-1')
        self.tempo.write_text('0.8')

    def MotorFreiaSobe(self):
        self.direcao.write_text('-1')
        self.tempo.write_text('0.8')

    def MotorAceleraDesce(self):
        self.direcao.write_text('1')
        self.tempo.write_text('0.8')

    def MotorFreiaDesce(self):
        self.direcao.write_text('1')
        self.tempo.write_text('0.8')


estados = [
    State('inicio'),
    State('parado'        , on_enter='PararMotor'),
    State('subindo'       , on_enter='MotorSubir'),
    State('acelera_sobe'  , on_enter='MotorAceleraSobe'),
    State('freia_sobe'    , on_enter='MotorFreiaSobe'),    
    State('descendo'      , on_enter='MotorDescer'),
    State('acelera_desce' , on_enter='MotorAceleraDesce'),
    State('freia_desce'   , on_enter='MotorFreiaDesce')
    ]

transicoes = [
    {'source':'inicio',        'trigger':'iniciar',    'dest':'parado'         },

    {'source':'parado',        'trigger':'subir',      'dest':'acelera_sobe'   },
    {'source':'acelera_sobe',  'trigger':'veloc',      'dest':'subindo'        },
    {'source':'acelera_sobe',  'trigger':'perto',      'dest':'freia_sobe'     },    
    {'source':'subindo',       'trigger':'perto',      'dest':'freia_sobe'     },
    {'source':'freia_sobe',    'trigger':'chegou',     'dest':'parado'         },

    {'source':'parado',        'trigger':'descer',     'dest':'acelera_desce'  },
    {'source':'acelera_desce', 'trigger':'veloc',      'dest':'descendo'       },
    {'source':'acelera_desce', 'trigger':'perto',      'dest':'freia_desce'    },    
    {'source':'descendo',      'trigger':'perto',      'dest':'freia_desce'    },
    {'source':'freia_desce',   'trigger':'chegou',     'dest':'parado'         },
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
