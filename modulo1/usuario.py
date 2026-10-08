
while True:
    nombre = input("Introduzca su nombre (solo letras): ")
    if len(nombre) in range(5,11) and nombre.isalpha():
        print("Nombre introducido correctamente")
        print(" ")
    
        while True:
            contrasena = input("Introduzca una contraseña con numeros y letras (min 8 caracteres): ")
            if len(contrasena)>7 and nombre.isalnum():
                print("Contraseña introducida correctamente")
                print(" ")
                print(f"Bienvenido {nombre}")
                print(" ")
                break
            else: 
                print ("error al introducir la contraseña")
        break
    else:
        print("error al introducir el nombre")




