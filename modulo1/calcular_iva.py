from funciones_iva import c_iva
from sys import exit
try:
    b1= float(input("Ingresa el bruto: "))
    p1= float(input("Ingrese el porcentaje: "))
    if 0 <= p1 <=100:
        print (f"Tienes que pagar {c_iva(b1, p1):.2f}")
    else:
        print("Error: El porcentaje debe de ser de 0 al 100")
except ValueError :
    print ("Valor no valido")
    exit (1)


    

