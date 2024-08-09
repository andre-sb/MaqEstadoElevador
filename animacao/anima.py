import time
import shutil
from pathlib import Path

terminal_size = shutil.get_terminal_size()
colunas = terminal_size.columns // 2
max_linhas = terminal_size.lines-3

linha = ' ' * colunas + '██████'
linhas = linha + '\n' + linha + '\n' + linha

pos = 0

while True:
    # Limpa o terminal e mostra o desenho
    print("\x1b[2J\x1b[H" + '\n' * pos + linhas, end='')

    direcao = int (Path('./direcao.txt').read_text())
    pos = (max_linhas+pos+direcao) % max_linhas

    tempo = float (Path('./tempo.txt').read_text())
    time.sleep(tempo)
