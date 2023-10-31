Dna = input("Digite uma sequência de DNA que corresponde entre as letras A, G, C e T: ").upper()
Rna= "" 

for base in Dna:
    if base == 'A':
        Rna += 'U'
    elif base == 'G': 
        Rna += 'C'
    elif base == 'C':
        Rna+= 'G'
    elif base == 'T':
        Rna+= 'A'
    else:
     print("Cadeia invalida")
    break
print(f"A sequência de RNA-m equivalente é: {Rna}")
