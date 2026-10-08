nombre= input("Escribe tu nombre:")
edad= int(input("Escribe tu edad:"))
lugar= input("Escribe tu lugar de nacimiento: ")


if edad < 20:
    print("¡Qué joven!")
elif 21 <= edad <= 35:
    print("No eres tan joven...")
elif edad > 35:
    print("¡Hay que empezar a cuidarse!")