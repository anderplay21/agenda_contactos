import json
import os
from contactos import Contacto, GestorContactos

def guardar(gestor, ruta_archivo):
    """Guardar todos los contactos en un archivo JSON"""

    #Convertir los contactos a una lista JSON
    datos = []
    for contacto in gestor.listar():
        datos.append({
            "nombre": contacto.nombre,
            "telefono": contacto.telefono,
            "email": contacto.email
        })

    #Crea la carpeta si no existe
    carpeta = os.path.dirname(ruta_archivo)
    if carpeta and not os.path.exists(carpeta):
        os.makedirs(carpeta)

        #Escribir los datos en el archivo
    with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=2, ensure_ascii=False)

    print(f"{len(datos)} contactos guardados en {ruta_archivo}")

def cargar(ruta_archivo):
    """Cargar contactos desde un archivo JSON"""

    # Si el archivo no existe, retorna un gestor vacío
    if not os.path.exists(ruta_archivo):
        print(f"No se encontró el archivo {ruta_archivo}. Se creará uno nuevo al guardar.")
        return GestorContactos()
    
    #Leer los datos del archivo
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        datos = json.load(archivo)
    
#Crear un nuevo gestor y agregar los contactos cargados
    gestor = GestorContactos()
    for item in datos:
        gestor.crear(item['nombre'], item['telefono'], item['email'])

    print(f"{len(datos)} contactos cargados desde {ruta_archivo}")
    return gestor