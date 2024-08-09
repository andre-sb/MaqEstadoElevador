# Uso: source anima.sh

((COLUNA=(COLUMNS/2)-5))
((MAX_LINHAS=LINES-3))

MARGEM=$(head -c $COLUNA /dev/zero | tr '\0' ' ')  # Sequência de $COLUNA espaços

tput civis # Oculta o cursor para ele não atrapalhar a animação
           # Para aparecer novamente use 'tput cnorm'

LINHA=0
while [[ 1 ]]
do
    sleep $(cat tempo.txt)

    direcao=$(cat direcao.txt)
    ((LINHA=(MAX_LINHAS+LINHA+direcao) % MAX_LINHAS))

    clear
    tput cup $LINHA 0
    printf "\
    $MARGEM██████
    $MARGEM██████
    $MARGEM██████"
done
