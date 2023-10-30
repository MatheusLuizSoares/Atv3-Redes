frase = input("Digite alguma frase: ")
vogais = 0
espaços = 0

for letra in frase:
    if letra in "aeiouAEIOU":
        vogais += 1
    if letra == " ":
        espaços += 1

print(f"A frase {frase} tem {vogais} vogais e {espaços} espaços em branco.")
