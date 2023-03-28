preco = float(input(("Digite o preço do produto: ")))

print("1 - À vista em dinheiro ou cheque, recebe 10% de desconto")
print("2 - À vista no cartão de crédito, recebe 15% de desconto")
print("3 - Em duas vezes, preço normal de etiqueta sem juros")
print("4 - Em duas vezes, preço normal de etiqueta mais juros de 10%")

pagamento = int(input("Digite de 1 a 4 para escolher a forma de pagamento: "))

if pagamento == 1:
    print(preco * 0.90)
elif pagamento == 2:
    print(preco * 0.85)
elif pagamento == 3:
    print(preco)
elif pagamento == 4:
    print(preco * 1.10)