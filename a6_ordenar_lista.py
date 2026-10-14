entrada = input("Ingresa números separados por comas: ")
lista_numeros = [float(num.strip()) for num in entrada.split(",")]
lista_numeros.sort()
print(lista_numeros)