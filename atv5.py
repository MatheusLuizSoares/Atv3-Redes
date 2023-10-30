Dna = input("Digite uma sequência de DNA que corresponde entre as letras A, G, C e T: ")
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

print(f"A sequência de RNA-m equivalente é: {Rna}")
