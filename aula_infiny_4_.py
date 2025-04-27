# Número que o jogador deve adivinhar
numero_secreto = 7

# Contador de tentativas
tentativas = 0

# Limite de tentativas
limite_tentativas = 2

while tentativas < limite_tentativas:
    palpite = int(input("Adivinhe o número (entre 1 e 10): "))
    tentativas += 1

    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número!")
        break
else:
    print("Que pena! Suas tentativas acabaram. O número era", numero_secreto)
