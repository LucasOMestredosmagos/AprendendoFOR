def gerar_tabuada(numero):
    if 1 <= numero <= 10:
        print(f"Tabuada do {numero}:")
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")
    else:
        print("Por favor, insira um número entre 1 e 10.")

numero = int(input("Informe um número entre 1 e 10 para ver a tabuada: "))
gerar_tabuada(numero)
