
cpf = input("Digite um CPF (11 dígitos numéricos): ")

cpf = cpf.replace(" ", "").replace("-", "")

if cpf.isdigit() and len(cpf) == 11:
    cpf = [int(d) for d in cpf]
    
    total = 0
    for i in range(9):
        total += cpf[i] * (10 - i)
    digito1 = (total * 10) % 11
    if digito1 != cpf[9]:
        print("CPF inválido.")
    else:

        total = 0
        for i in range(10):
            total += cpf[i] * (11 - i)
        digito2 = (total * 10) % 11
        if digito2 != cpf[10]:
            print("CPF inválido.")
        else:
            print("CPF válido.")
else:
    print("CPF inválido. Deve conter 11 dígitos numéricos.")
