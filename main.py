def matriz_respostas():
    jogo = [["Água", "Água", "Água", "Água", "Água", "Água", "Água", "Água", "Água"],
            ["Água", "Navio", "Água", "Navio", "Água", "Água", "Água", "Água", "Água"],
            ["Água", "Água", "Água", "Navio", "Água", "Água", "Água", "Água", "Água"],
            ["Água", "Água", "Água", "Água", "Navio", "Água", "Água", "Água", "Água"],
            ["Água", "Água", "Água", "Água", "Água", "Água", "Água", "Água", "Água"],
            ["Água", "Navio", "Água", "Navio", "Água", "Água", "Água", "Água", "Navio"],
            ["Navio", "Água", "Navio", "Água", "Água", "Navio", "Água", "Navio", "Água"],
            ["Água", "Água", "Navio", "Navio", "Água", "Água", "Navio", "Água", "Navio"],
            ["Navio", "Navio", "Água", "Água", "Navio", "Navio", "Água", "Água", "Navio"]]
    return jogo

def matriz_ataque():
    jogo_ataque = [["*", "*", "*", "*", "*", "*", "*", "*", "*"],
                   ["*", "*", "*", "*", "*", "*", "*", "*", "*"],
                   ["*", "*", "*", "*", "*", "*", "*", "*", "*"],
                   ["*", "*", "*", "*", "*", "*", "*", "*", "*"],
                   ["*", "*", "*", "*", "*", "*", "*", "*", "*"],
                   ["*", "*", "*", "*", "*", "*", "*", "*", "*"],
                   ["*", "*", "*", "*", "*", "*", "*", "*", "*"],
                   ["*", "*", "*", "*", "*", "*", "*", "*", "*"],
                   ["*", "*", "*", "*", "*", "*", "*", "*", "*"]]

    return jogo_ataque


while True:
    while True:
        while True:
            linha = int(input("Digite o número da linha que deseja: "))
            if linha > 8:
                print("Valor %d inválido. Digite um número de 0 a 8." % linha)
                continue
            break

        while True:
            coluna = int(input("Digite o número da coluna que deseja: "))
            if coluna > 8:
                print("Valor %d inválido. Digite um número de 0 a 8." % coluna)
                continue
            break
