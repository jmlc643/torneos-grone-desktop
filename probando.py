equipos = ["Alianza Lima", "Universitario", "Cristal", "Melgar", "Boys", "Cienciano", "ADT"]

def generar_fixture(n = []):

    nro_equipos = len(n)

    if len(n) % 2 != 0:
        nro_equipos = len(n) + 1  # Agregar un equipo ficticio (X) si la cantidad de equipos es impar

    equipo_descansa = f'{nro_equipos}'  # Número del equipo ficticio (puedes ajustar esto según tus preferencias)
    equipos.append(equipo_descansa)

    # Generar el fixture
    for i in range(nro_equipos - 1):
        print("\nFecha", i + 1)
        mitad = int(nro_equipos / 2)
        local = n[:mitad]
        visitante = n[mitad:][::-1]  # Invertir el orden

        for l, v in zip(local, visitante):
            """
            Zip se usa para concatenar elementos de 2 listas en una lista de tuplas
            por ejemplo [1, 2, 3] y [4, 5, 6] se concatena de la siguiente manera
            [(1,4),(2,5),(3,6)]
            """
            if v != equipo_descansa:
                if l != equipo_descansa:
                    print(f"{l} vs {v}")
                else:
                    print(f'{v} descansa')
            else:
                print(f"{l} descansa")


        # Rotar los equipos en sentido antihorario
        n = [n[0]] + n[mitad + 1:] + n[1:mitad + 1]

# Ejemplo con 4 equipos
generar_fixture(equipos)