num1 = int(input("Escreva um número: "))
num2 = int(input("Escreva outro número: "))
num3 = int(input("Escreva outro número: "))

if num1 >= num2 and num2 >= num3:
    print(f"A ordem decrescente é {num3}, {num2}, {num1}")
elif num1 > num3 and num3 > num2:
    print(f"A ordem decrescente é {num1}, {num3}, {num2}")
elif num2 > num1 and num1 > num3:
    print(f"A ordem decrescente é {num2}, {num1}, {num3}")
elif num2 > num3 and num3 > num1:
    print(f"A ordem decrescente é {num2}, {num3}, {num1}")
elif num3 > num2 and num2 > num1:
    print(f"A ordem decrescente é {num3}, {num2}, {num1}")
elif num3 > num1 and num1 > num2:
    print(f"A ordem decrescente é {num3}, {num1}, {num2}")
else:
    print("PROCURE DEUS!!!")