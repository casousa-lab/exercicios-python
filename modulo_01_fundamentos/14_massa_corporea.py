peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))
massa = peso / (altura * altura)

if massa < 26:
    print("Normal")
elif massa <= 30:
    print("Obeso")
else:
    print("Obeso Mórbido")