nome = input("Nome do cliente: ")
total = 0

qtd = int(input("Quantos Hot Dog: "))
total += qtd * 11.20
qtd = int(input("Quantos Hamburguer: "))
total += qtd * 16.60
qtd = int(input("Quantos Cheeseburguer: "))
total += qtd * 22.00
qtd = int(input("Quantos Refrigerantes em lata: "))
total += qtd * 8.00
qtd = int(input("Quantas Batatas fritas: "))
total += qtd * 32.50
qtd = int(input("Quantos Misto quente: "))
total += qtd * 13.00
qtd = int(input("Quantos Sucos naturais: "))
total += qtd * 8.00

print(f"Cliente: {nome}")
print(f"Total do pedido: R$ {total:.2f}")