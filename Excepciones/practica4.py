"""
Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción
FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario.
Sin embargo, también intenta crear el archivo si no existe.
"""
nombre_archivo = input("Ingrese el nombre del archivo: ")

try:
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()
        print(f"Contenido del archivo '{nombre_archivo}':\n{contenido}")
except FileNotFoundError as e:
    print(f"Ha ocurrido un error, el archivo '{nombre_archivo}' no existe.")
    print(f"Detalles del error: {e}")
    print(f"Intentando crear el archivo '{nombre_archivo}'")
    try:
        with open(nombre_archivo, 'w') as archivo_creado:
            archivo_creado.write("Se ha creado un nuevo archivo de forma automática.")
        print(f"El archivo '{nombre_archivo}' ha sido creado exitosamente.")
    except Exception as e:
        print(f"Ha ocurrido un error en la crecion del archivo '{nombre_archivo}'")
        print(f"Detalles del error: {e}")
        