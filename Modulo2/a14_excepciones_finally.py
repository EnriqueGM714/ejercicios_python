try:
    archivo = open("archivo_inexistente.txt", "r")
except FileNotFoundError:
    print("Error: Archivo no encontrado.")
finally:
    print("El bloque finally se ha ejecutado.")