altura = float(input("Digite sua altura em metros: "))
sexo = int(input("Digite 1 para sexo masculino e 2 para feminino: "))
pesoM = (altura * 72.7) - 58
pesoF = (altura * 62.1) - 44.7

if sexo == 1:
    print(f"Seu peso ideal é {pesoM}")
elif sexo == 2:
    print(f"Seu peso ideal é {pesoF}")
else:
    print("PROCURE DEUS!!!")