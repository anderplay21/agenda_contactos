# importamos las funciones y clases necesarias
from contactos import GestorContactos
from almacenamiento import guardar, cargar
from menu import (
    mostrar_menu, 
    obtener_opcion, 
    pedir_datos_contacto,
    mostrar_contacto,
    mostrar_lista_contactos
)

# Función principal que orquesta toda la aplicación
def main():
    """Función principal que orquesta toda la aplicación"""
    
    # Archivo donde guardaremos los contactos
    ARCHIVO_DATOS = "datos/contactos.json"
    
    # Cargar contactos guardados (o iniciar vacío)
    print("Cargando agenda...")
    agenda = cargar(ARCHIVO_DATOS)
    
    # Bucle principal
    while True:
        try:
            # Mostrar menú y obtener opción
            mostrar_menu()
            opcion = obtener_opcion()
            
            # OPCIÓN 1: Crear contacto
            if opcion == "1":
                print("\n--- CREAR CONTACTO ---")
                nombre, telefono, email = pedir_datos_contacto()
                
                # Validar que no esté vacío
                if not nombre or not telefono or not email:
                    print("❌ Todos los campos son obligatorios.")
                    continue
                
                # Validar que no exista ya
                if agenda.buscar(nombre):
                    print(f"❌ El contacto '{nombre}' ya existe.")
                    continue
                
                # Crear
                agenda.crear(nombre, telefono, email)
                print(f"✅ Contacto '{nombre}' creado exitosamente.")
            
            # OPCIÓN 2: Ver todos
            elif opcion == "2":
                mostrar_lista_contactos(agenda.listar())
            
            # OPCIÓN 3: Buscar contacto
            elif opcion == "3":
                print("\n--- BUSCAR CONTACTO ---")
                nombre = input("Nombre del contacto: ").strip()
                
                contacto = agenda.buscar(nombre)
                if contacto:
                    mostrar_contacto(contacto)
                else:
                    print(f"❌ Contacto '{nombre}' no encontrado.")
            
            # OPCIÓN 4: Editar contacto
            elif opcion == "4":
                print("\n--- EDITAR CONTACTO ---")
                nombre = input("Nombre del contacto a editar: ").strip()
                
                # Verificar que existe
                if not agenda.buscar(nombre):
                    print(f"❌ Contacto '{nombre}' no encontrado.")
                    continue
                
                # Pedir nuevos datos (pueden estar vacíos para no cambiar)
                print("(Deja vacío si no quieres cambiar)")
                nuevo_telefono = input("Nuevo teléfono: ").strip()
                nuevo_email = input("Nuevo email: ").strip()
                
                # Editar
                agenda.editar(nombre, nuevo_telefono or None, nuevo_email or None)
                print(f"✅ Contacto '{nombre}' actualizado.")
            
            # OPCIÓN 5: Eliminar contacto
            elif opcion == "5":
                print("\n--- ELIMINAR CONTACTO ---")
                nombre = input("Nombre del contacto a eliminar: ").strip()
                
                # Pedir confirmación
                confirmacion = input(f"¿Estás seguro de eliminar '{nombre}'? (s/n): ").lower()
                
                if confirmacion == "s":
                    if agenda.eliminar(nombre):
                        print(f"✅ Contacto '{nombre}' eliminado.")
                    else:
                        print(f"❌ Contacto '{nombre}' no encontrado.")
                else:
                    print("❌ Operación cancelada.")
            
            # OPCIÓN 6: Guardar y salir
            elif opcion == "6":
                guardar(agenda, ARCHIVO_DATOS)
                print("\n👋 ¡Hasta luego!")
                break
            
            # Opción inválida
            else:
                print("❌ Opción inválida. Elige un número del 1 al 6.")
        
        except KeyboardInterrupt:
            # Cuando el usuario presiona Ctrl+C
            print("\n\n⚠️  Programa interrumpido por el usuario.")
            guardar(agenda, ARCHIVO_DATOS)
            print("👋 ¡Hasta luego!")
            break
        
        except Exception as e:
            # Cualquier otro error inesperado
            print(f"❌ Error inesperado: {e}")
            print("Por favor, intenta de nuevo.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()