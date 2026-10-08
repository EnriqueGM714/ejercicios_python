from funciones_usuario import *

n1= input("Introduce tu nombre: ")
a1= input("Introduce tus apellidos: ")
e1= int(input("Introduce tu edad: "))

print(get_nombre_completo(n1, a1))
print(get_nombre_y_edad(get_nombre_completo(n1,a1), e1))