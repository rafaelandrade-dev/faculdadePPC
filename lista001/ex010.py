id = input("Digite seu nome: ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

mediaE = (nota1 + nota2 + nota3) / 3

mediaA = (nota1 + nota2 * 2 + nota3 * 3 + mediaE)/7

if mediaA >= 90:
    conceito = ("A")
elif mediaA >= 75 and mediaA < 90:
    conceito = ("B")
elif mediaA >= 60 and mediaA < 75:
    conceito = ("C")
elif mediaA >= 40 and mediaA < 60:
    conceito = ("D")
elif mediaA < 40:
    conceito = ("E")
else:
    print("Você fez algo muito errado, tente novamente.") 


print(f"Aluno: {id}")
print(f"Nota 1: {nota1}", f"Nota 2: {nota2}", f"Nota 3: {nota3}")
print(f"Sua média nas avaliações foi de {mediaE}")
print(f"Sua média de aproveitamento foi de {mediaA}")
print(f"Sua média de aproveitamento Conceito foi {conceito}")

if conceito == "A" or conceito == "B" or conceito == "C":
    print("Você foi aprovado")
else: 
    print("Você foi reprovado! Estude mais da próxima vez.")