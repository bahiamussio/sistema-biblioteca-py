# Clase Biblioteca
from clases.libros import Libro
from clases.prestamos import Prestamo
from clases.usuarios import Usuario


class Biblioteca:
    def __init__(self):
        # Lista inicial de libros de la biblioteca
        self.libros = [
            Libro("1984", "George Orwell"),
            Libro("Cien años de soledad", "Gabriel García Márquez"),
            Libro("Don Quijote de la Mancha", "Miguel de Cervantes"),
            Libro("La casa de los espíritus", "Isabel Allende"),
            Libro("Crimen y castigo", "Fyodor Dostoevsky"),
            Libro("El gran Gatsby", "F. Scott Fitzgerald"),
            Libro("Orgullo y prejuicio", "Jane Austen"),
            Libro("El principito", "Antoine de Saint-Exupéry"),
            Libro("Matar a un ruiseñor", "Harper Lee"),
            Libro("Ulises", "James Joyce"),
        ]
        # Lista inicial de usuarios
        self.usuarios = [
            Usuario("Juan Pérez", 12345678),
            Usuario("Ana Gómez", 23456789),
        ]
        self.prestamos = []  # Lista de préstamos

    # Mostrar los libros existentes en la biblioteca
    def mostrar_libros(self):
        print("\nLista de Libros Disponibles:")
        for libro in self.libros:
            print(f"- {libro.titulo} de {libro.autor}")

    # Registrar un libro
    def registrar_libro(self, titulo, autor):
        libro = Libro(titulo, autor)
        self.libros.append(libro)  # Agregar el nuevo libro a la lista existente
        print(f"El libro '{titulo}' ha sido registrado exitosamente.")

    # Registrar Usuario
    def registrar_usuario(self, nombre, dni):
        # Verificar si el DNI ya está registrado
        if any(u.dni == dni for u in self.usuarios):
            print(f"El usuario con DNI {dni} ya está registrado.")
        else:
            usuario = Usuario(nombre, dni)
            self.usuarios.append(usuario)
            print(f"El usuario {nombre} con DNI {dni} ha sido registrado.")

    # Prestar un libro a un usuario
    def prestar_libro(self, dni, titulo):
        usuario = next((u for u in self.usuarios if u.dni == dni), None)
        libro = next((l for l in self.libros if l.titulo.lower().strip() == titulo.lower().strip() and l.disponible), None)
        if usuario and libro:
            libro.disponible = False
            prestamo = Prestamo(usuario, libro)  # Crear un objeto Prestamo
            usuario.prestamos.append(prestamo)  # Agregar el préstamo al usuario
            print(
                f"El libro '{titulo}' ha sido prestado a {usuario.nombre}. Fecha de préstamo: {prestamo.fecha_prestamo.strftime('%d/%m/%Y %H:%M:%S')}."
            )
        else:
            print(
                "No se puede realizar el préstamo. Verifica que el libro esté disponible y el usuario esté registrado."
            )

    # Devolver un libro
    def devolver_libro(self, dni, titulo):
        usuario = next((u for u in self.usuarios if u.dni == dni), None)
        prestamo = next(
            (
                p
                for p in usuario.prestamos
                if p.libro.titulo == titulo and p.fecha_devolucion is None
            ),
            None,
        )
        if usuario and prestamo:
            prestamo.devolver_libro()  # Devolver el libro y registrar la fecha
            prestamo.libro.disponible = True  # Marcar el libro como disponible
            print(
                f"El libro '{titulo}' ha sido devuelto por {usuario.nombre}. Fecha de devolución: {prestamo.fecha_devolucion.strftime('%d/%m/%Y %H:%M:%S')}."
            )
        else:
            print(
                "No se puede devolver el libro. Verifica que el libro esté prestado al usuario."
            )

    # Método para mostrar los usuarios que han solicitado libros
    def mostrar_usuarios_prestados(self):
        for usuario in self.usuarios:
            if usuario.prestamos:  # Si el usuario tiene algún préstamo
                libros_prestados = [
                    prestamo.libro.titulo for prestamo in usuario.prestamos
                ]
                print(
                    f"{usuario.nombre} ha solicitado los siguientes libros: {', '.join(libros_prestados)}."
                )
            else:
                print(f"{usuario.nombre} no ha solicitado libros.")

    # Método para mostrar los usuarios registrados
    def mostrar_usuarios(self):
        print("\nLista de Usuarios Registrados:")
        for usuario in self.usuarios:
            print(f"- {usuario.nombre}, DNI: {usuario.dni}")