# AGENDA DE CONTACTOS

Este proyecto tiene como objetivo desarrollar mis habilidades en programacion con python.
Mi principal objetivo es aprender y poner en practica lo aprendido en cursos de programacion.

Esta agenda de contactos debe contar con las siguientes especificaciones:

1- Buscar contactos.
2- Agregar contactos nuevos.
3- Visualizar la lista de contactos guardados.
4- El usuario puede eliminar contactos agregados previamente.
5- El usuario puede editar un contacto guardado anteriormente.
6- El usuario puede exportar la lista de contacto guardados en un archivo json

Para este proyecto voy a aplicar la regla de separacion de responsabilidades por esto
la estructura de archivos esta distribuida de la siguiente manera:

agenda_contactos/
│
├── main.py              # Punto de entrada — aquí arranca el programa
├── contactos.py         # Lógica: agregar, buscar, eliminar contactos
├── almacenamiento.py    # Leer y guardar contactos en un archivo
├── datos/
│   └── contactos.json   # Aquí se guardan los contactos
└── README.md            # Descripción del proyecto

¿Que hace cada archivo?

## main.py — Es el menú principal, el que el usuario ve:
# Ejemplo de lo que irá aquí
# "1. Agregar contacto"
# "2. Buscar contacto"
# "3. Salir"

## contactos.py — Contiene las funciones de negocio:
def agregar_contacto(nombre, telefono): ...
def buscar_contacto(nombre): ...
def eliminar_contacto(nombre): ...

##  almacenamiento.py — Se encarga de persistir los datos:

def cargar_contactos(): ...   # Lee el .json
def guardar_contactos(): ...  # Escribe en el .json

## contactos.json — Así lucirán tus datos guardados:

[
  {"nombre": "Ana García", "telefono": "3001234567"}
]



