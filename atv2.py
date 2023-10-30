d = input("Digite uma frase qualquer: ")
cara = input("Digite o caractere que você quer contar: ")

n = 0
espacos = 0

for letra in d:
    n += 1
    if letra == ' ':
        espacos += 1
        
if cara in d:
    quantidade_cara = d.count(cara)
    print(f"O caractere '{cara}' apareceu {quantidade_cara} vezes na frase.")
    print(f"O número de espaços na frase é {espacos}.")
