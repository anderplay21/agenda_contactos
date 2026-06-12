def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*40)
    print("     AGENDA DE CONTACTOS")
    print("="*40)
    print("1. Crear contacto")
    print("2. Ver todos los contactos")
    print("3. Buscar contacto")
    print("4. Editar contacto")
    print("5. Eliminar contacto")
    print("6. Guardar y salir")
    print("="*40)


def obtener_opcion():
    """Obtiene la opción del usuario"""
    opcion = input("Elige una opción (1-6): ").strip()
    return opcion


def pedir_datos_contacto():
    """Pide los datos para crear/editar un contacto"""
    nombre = input("Nombre: ").strip()
    telefono = input("Teléfono: ").strip()
    email = input("Email: ").strip()
    
    return nombre, telefono, email


def mostrar_contacto(contacto):
    """Muestra un contacto formateado"""
    print("-" * 40)
    print(f"Nombre:   {contacto.nombre}")
    print(f"Teléfono: {contacto.telefono}")
    print(f"Email:    {contacto.email}")
    print("-" * 40)


def mostrar_lista_contactos(contactos):
    """Muestra todos los contactos en una lista"""
    if not contactos:
        print("\n⚠️  No hay contactos guardados.")
        return
    
    print("\n" + "="*40)
    print("LISTA DE CONTACTOS")
    print("="*40)
    for i, contacto in enumerate(contactos, 1):
        print(f"{i}. {contacto}")
    print("="*40)