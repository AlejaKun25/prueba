import csv
import numpy as np

peliculas = []
asientos = np.zeros((15, 10), dtype=int)
valor_entrada = 2000

# Película predeterminada
pelicula_predeterminada = {
    "nombre": "Spider Man - Lejos de Casa",
    "descripcion": "Una película del Hombre Araña",
    "categoria": "Acción",
    "ventas": 0,
    "asistentes": 0,
    "asistentes_lista": []
}
peliculas.append(pelicula_predeterminada)

def mostrar_asientos(pelicula_index):
    if pelicula_index < 0 or pelicula_index >= len(peliculas):
        print("La película seleccionada no es válida.")
        return

    pelicula = peliculas[pelicula_index]
    print(f"Estado de los asientos para la película: {pelicula['nombre']}")
    if pelicula['asistentes'] == 0:
        print("No hay asientos ocupados.")
        return

    print("   1  2  3  4  5  6  7  8  9  10")
    for i, fila in enumerate(asientos):
        print(f"{i+1:2d} ", end="")
        for j, asiento in enumerate(fila):
            if asiento == 0:
                print("[℗]", end=" ")
            else:
                print("[✌]", end=" ")
        print()

def mostrar_peliculas():
    if len(peliculas) == 0:
        print("No hay películas registradas.")
    else:
        for i, pelicula in enumerate(peliculas):
            print(f"{i+1}. {pelicula['nombre']} - {pelicula['categoria']}")

def comprar_entrada(pelicula_index):
    if pelicula_index < 0 or pelicula_index >= len(peliculas):
        print("La película seleccionada no es válida.")
        return

    pelicula = peliculas[pelicula_index]
    mostrar_asientos(pelicula_index)

    fila_str = input("Ingrese el número de fila del asiento: ")
    if not fila_str.isdigit():
        print("El número de fila debe ser un número entero.")
        return
    fila = int(fila_str)

    columna_str = input("Ingrese el número de columna del asiento: ")
    if not columna_str.isdigit():
        print("El número de columna debe ser un número entero.")
        return
    columna = int(columna_str)

    if fila < 1 or fila > 15 or columna < 1 or columna > 10:
        print("El asiento seleccionado no es válido.")
        return

    if asientos[fila-1, columna-1] == 0:
        asientos[fila-1, columna-1] = 1
        pelicula["ventas"] += 1
        pelicula["asistentes"] += 1
        pelicula["asistentes_lista"].append(input("Ingrese el nombre del Cliente: "))
        num_boleta = len(pelicula["asistentes_lista"],)
        generar_boucher(pelicula["nombre"], fila, columna, num_boleta)
        print("¡Compra exitosa! Se ha generado el boletín.")
    else:
        print("El asiento seleccionado ya está ocupado.")

def generar_boucher(nombre_pelicula, fila, columna, num_boleta):
    with open(f"boucher_{num_boleta}.txt", "w") as archivo:
        archivo.write(f"--- Boucher de Compra ---\n")
        archivo.write(f"Película: {nombre_pelicula}\n")
        archivo.write(f"Asiento: Fila {fila}, Columna {columna}\n")
        archivo.write(f"Valor de entrada: {valor_entrada}\n")
        archivo.write(f"Número de boleta: {num_boleta}\n")
        archivo.write(f"-------------------------\n")

# Película predeterminada
asientos[5, 3] = 1
pelicula_predeterminada["ventas"] += 1
pelicula_predeterminada["asistentes"] += 1
pelicula_predeterminada["asistentes_lista"].append("Benjamin Mora")

# Menú principal
while True:
    print("************************")
    print("****    CINEDUOC    ****")
    print("************************")
    print("1. Mostrar asientos")
    print("2. Mostrar películas")
    print("3. Comprar entrada")
    print("0. Salir")

    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        mostrar_asientos(int(input("Ingrese el número de película: ")) - 1)
    elif opcion == "2":
        mostrar_peliculas()
    elif opcion == "3":
        comprar_entrada(int(input("Ingrese el número de película: ")) - 1)
    elif opcion == "0":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente nuevamente.")