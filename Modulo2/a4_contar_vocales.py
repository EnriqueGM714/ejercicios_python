palabra = input("Ingresa una palabra: ")
vocales = sum(1 for letra in palabra.lower() if letra in "aeiouáéíóú")
print(vocales)