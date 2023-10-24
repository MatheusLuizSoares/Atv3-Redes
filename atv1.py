d=str(input("Digite uma frase quaisquer:"))
cara=str(input("Digite a um carater qeu parece no texto"))

n=0
posição=0
for letra in d:
 n+=1

if cara in d:
      print(f"apareceu desta quantidade:{n}")