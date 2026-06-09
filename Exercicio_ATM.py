valor = int(input("Digite o valor a ser sacado: "))
cedulas = [100, 50, 20, 10, 5, 2, 1]
quantidade_cedulas = {}
for cedula in cedulas:
    quantidade_cedulas[cedula] = valor // cedula
    valor = valor % cedula
print("Quantidade de cédulas necessárias:")
for cedula in cedulas:
    if quantidade_cedulas[cedula] > 0:
        print(f"{quantidade_cedulas[cedula]} cédula(s) de R${cedula}")
        