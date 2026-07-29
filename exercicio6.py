"""
Jogo da adivinhação da palavra
"""

palavra_secreta = "Computador"

if palavra_secreta[0].isupper() is True:
    print("A palavra começa com letra maiúscula")
else:
    print("A palavra não começa com letra maiúscula")

print(f"Dica: a palavra secreta começa com {palavra_secreta[0]}")

palavra_do_usuario = ''
tentativas = 0

for letra in palavra_secreta:
    tentativas = int(tentativas)
    tentativas += 1

    letra = input("Digite uma letra: ")

    if letra.isdigit() is True:
        print("Você não digitou um caractere válido. Programa encerrado")
        break

    if len(letra) > 1:
        print("Você digitou mais de uma letra")
        break

    if letra not in palavra_secreta:
        print("Esta letra não está na palavra secreta")
        palavra_do_usuario = palavra_do_usuario + '*'
        print(palavra_do_usuario)
        continue

    else:
        print(f'A letra digitada foi: {letra}')
        palavra_do_usuario = palavra_do_usuario + letra
        print(palavra_do_usuario)
        print(f'Tentativas: {tentativas}x')
        continue


palavra_do_usuario.capitalize()

if palavra_do_usuario == palavra_secreta:
    print("Parabéns! Você descobriu a palavra")
else:
    print(f"Você não descobriu a palavra. A palavra era: {palavra_secreta}")