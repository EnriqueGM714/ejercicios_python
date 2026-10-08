try:
    num= float(input("Escribe el numerador de tu división: "))
    print(" ")
    den= float(input("Escribe el denominador de tu división: "))
    res= num/den
    print(" ")
    print(f"El resultado de tu division es {res:.2f}")
except ValueError:
    print("VALORES INTRODUCIDOS INCORRECTOS")
except ZeroDivisionError:
    print("NO SE PUEDE DIVIDIR POR CERO")
