import json

# -----------------------------
# LISTAR CINES
# -----------------------------
def listarCines():
    """Devuelve todos los cines en forma de lista de tuplas (id, nombre, direccion)."""
    try:
        with open("cines.json", "r") as file:
            cines = json.load(file)
    except FileNotFoundError:
        print("Error: No se encontró el archivo de cines.")
        return []

    # Usamos list comprehension + tupla para devolver (id, nombre, direccion)
    listado = [(cid, data["nombre"].strip(), data["direccion"].strip()) for cid, data in cines.items()]

    # Mostramos como tabla formateada usando cadenas
    print("\n--- LISTADO DE CINES ---")
    for cid, nombre, direccion in listado:
        print(f"ID: {cid:<3} | Nombre: {nombre:<25} | Dirección: {direccion}")

    return listado


# -----------------------------
# INFORME LISTADO DE PELÍCULAS DISPONIBLES
# -----------------------------
def informeListadoPeliculasDisponibles():
    """Muestra todas las películas activas, con idiomas y formatos sin duplicados por cine."""
    try:
        with open("movies.json", "r") as file:
            movies = json.load(file)
    except FileNotFoundError:
        print("Error: No se encontró el archivo de películas.")
        return []

    disponibles = [
        (mid, data["title"].strip(), data["language"], data["format"], data.get("cineId", "N/A"))
        for mid, data in movies.items()
        if data.get("activo", True)  # filtramos con comprensión de listas
    ]

    if not disponibles:
        print("No hay películas disponibles actualmente.")
        return []

    # Conjuntos para eliminar duplicados de idiomas y formatos
    idiomas = {pelicula[2] for pelicula in disponibles}
    formatos = {pelicula[3] for pelicula in disponibles}

    print("\n--- LISTADO DE PELÍCULAS DISPONIBLES ---")
    for mid, titulo, idioma, formato, cineId in disponibles:
        print(f"ID: {mid:<4} | Título: {titulo:<25} | Idioma: {idioma:<10} | Formato: {formato:<3} | Cine: {cineId}")

    print("\nIdiomas únicos disponibles:", ", ".join(sorted(idiomas)))
    print("Formatos únicos disponibles:", ", ".join(sorted(formatos)))

    return disponibles


# -----------------------------
# NUEVO CINE
# -----------------------------
def nuevoCine():
    """Agrega un nuevo cine usando tupla (nombre, direccion)."""
    try:
        with open("cines.json", "r") as file:
            cines = json.load(file)
    except FileNotFoundError:
        cines = {}

    # Pedimos datos al usuario
    nombre = input("Ingrese el nombre del cine: ").strip()
    direccion = input("Ingrese la dirección del cine: ").strip()

    # Guardamos temporalmente en una tupla
    cine_data = (nombre, direccion)

    # Creamos el próximo ID automáticamente
    nuevo_id = str(int(max(cines.keys(), default="0")) + 1)

    # Convertimos tupla en diccionario para guardar
    cines[nuevo_id] = {"nombre": cine_data[0], "direccion": cine_data[1]}

    with open("cines.json", "w") as file:
        json.dump(cines, file, indent=4)

    print(f"\n✅ Cine agregado con éxito: {nombre} (ID: {nuevo_id})")
    return nuevo_id


"""
listarCines() → usa tuplas, list comprehension, formateo de cadenas.

informeListadoPeliculasDisponibles() → usa list comprehension para filtrar, devuelve tuplas, usa set para eliminar duplicados, cadenas para formatear salida.

nuevoCine() → usa una tupla temporal (nombre, direccion), luego la convierte en diccionario, y formatea cadenas.

"""