import random

def escolher_palavra():
    palavras = ["desenvolvimento", "tecnologia", "programacao", "tendencias"]
    return random.choice(palavras)
def exibir_forca(tentativas):
    forca = [
        "  ____  ",
        " |    | ",
        " |      ",
        " |      ",
        " |      ",
        " |      ",
        " |      ",
        "_|__    "
    ]

    if tentativas == 1:
        forca[2] = " |    O "
    elif tentativas == 2:
        forca[3] = " |    | "
    elif tentativas == 3:
        forca[3] = " |   /| "
    elif tentativas >= 4:
        forca[3] = " |   /|\\"
    if tentativas == 5:
        forca[4] = " |   /  "
    elif tentativas >= 6:
        forca[4] = " |   / \\"

    for linha in forca:
        print(linha)


def jogar():
    palavra = escolher_palavra()
    palavra_oculta = ["_" for _ in palavra]
    letras_tentadas = []
    tentativas = 0

    print("Bem-vindo ao jogo da Forca!")
    print("Tente adivinhar a palavra secreta.")
    print("")

    while tentativas < 6:
        letra = input("Digite uma letra: ").lower()

        if letra in letras_tentadas:
            print("Você já tentou esta letra. Tente outra.")
            continue

        letras_tentadas.append(letra)

        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_oculta[i] = letra
            print("Letra correta!")
        else:
            tentativas += 1
            print("Letra incorreta!")

        exibir_forca(tentativas)
        print("Palavra: ", " ".join(palavra_oculta))

        if "_" not in palavra_oculta:
            print("Parabéns! Você ganhou!")
            return

    print("Você perdeu! A palavra era:", palavra)


jogar()
