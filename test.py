from menu import mostrar_menu, pedir_datos_contacto, mostrar_lista_contactos, mostrar_contacto
from contactos import Contacto

# Crear un contacto de ejemplo
contacto_ejemplo = Contacto("Anderson", "3000454400", "anderson@gmail.com")

lista_ejemplo = [contacto_ejemplo]
mostrar_lista_contactos(lista_ejemplo)
