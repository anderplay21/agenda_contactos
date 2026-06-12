class Contacto:
    """Representa un contacto individual"""
    
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
    
    def __str__(self):
        return f"{self.nombre} | {self.telefono} | {self.email}"


class GestorContactos:
    """Gestiona la lista completa de contactos"""
    
    def __init__(self):
        self.contactos = []
    
    def crear(self, nombre, telefono, email):
        """Crea un nuevo contacto"""
        nuevo_contacto = Contacto(nombre, telefono, email)
        self.contactos.append(nuevo_contacto)
        return nuevo_contacto
    
    def listar(self):
        """Retorna todos los contactos"""
        return self.contactos
    
    def buscar(self, nombre):
        """Busca un contacto por nombre"""
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                return contacto
        return None
    
    def eliminar(self, nombre):
        """Elimina un contacto por nombre"""
        contacto = self.buscar(nombre)
        if contacto:
            self.contactos.remove(contacto)
            return True
        return False
    
    def editar(self, nombre, nuevo_telefono=None, nuevo_email=None):
        """Edita un contacto existente"""
        contacto = self.buscar(nombre)
        if contacto:
            if nuevo_telefono:
                contacto.telefono = nuevo_telefono
            if nuevo_email:
                contacto.email = nuevo_email
            return True
        return False