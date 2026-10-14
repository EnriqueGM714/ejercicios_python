try:
    resultado = 5/0
    numero=int(input("Escribe un numero "))
    print(numero)
except ValueError:
    print("No has ingresado un numero")
except ZeroDivisionError:
    print("Error: No se puede dividir entre 0.") 