videojuegos = ["Super Mario", "Zelda", "Minecraft", "Tetris", "Dark Souls"]
busqueda = input("Busca un videojuego: ")
if busqueda.lower() in [juego.lower() for juego in videojuegos]:
    print("El videojuego está en la lista.")
else:
    print("El videojuego no está en la lista.")