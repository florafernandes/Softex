#Simulação de eleição.
def votacao(candidato):  # função para votação com a variavel candidato como argumento
    global candidato_X, candidato_Y, candidato_Z, nulos
 
    if candidato.isalpha():  # checa se candidato contem apenas letras
        if candidato == 'Fim' or candidato == 'fim' or candidato == 'FIM':
            print('FIM DA VOTAÇÃO')
            print_resultados()

    elif candidato.isnumeric():  # checa se candidato e um caracter numerico
        if candidato == '889' or candidato == '847' or candidato == '515':
            if candidato == '889':
                candidato_X += 1
            elif candidato == '847':
                 candidato_Y += 1
            elif candidato == '515':
                 candidato_Z += 1
        elif candidato == '0':
            nulos += 1
        else:  # se o valor digitado nao e valido, há entrada de novo candidato e a funcao repete
            candidato= str(input('Digite um numero valido para o candidato: '))
            votacao(candidato)


def print_resultados():  # printa resultados e encerra programa
    global candidato_X, candidato_Y, candidato_Z, nulos

    print('QUANTIDADE DE VOTOS:\n')
    print('CANDIDATO X - TOTAL DE ' + str(candidato_X))
    print('CANDIDATO Y - TOTAL DE ' + str(candidato_Y))
    print('CANDIDATO Z - TOTAL DE ' + str(candidato_Z))
    print ('BRANCOS OU NULOS - TOTAL DE ' + str (nulos))

    exit()  # encerra prog


if __name__ == '__main__':  # funcao main 
    candidato_X = 0
    candidato_Y = 0
    candidato_Z = 0
    nulos = 0

    while True:  # laço ocorre indefinidamente ate que ocorra o 'Fim'
        candidato = str(input('ELEIÇÃO ESPECIAL\nDigite o numero correspondente do seu candidato:\n Candidato X -> 889\n Candidato Y -> 847\n Candidato Z -> 515\n Voto Branco -> 0\n Digite FIM para sair da votação e imprimir o resultado.'))
        votacao(candidato)