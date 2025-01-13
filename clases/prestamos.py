from datetime import datetime

# Clase Prestamo
class Prestamo:
    def __init__(self, usuario, libro):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = datetime.now()  # Fecha y hora del préstamo
        self.fecha_devolucion = None  # Se asignará cuando se devuelva el libro

    def devolver_libro(self):
        self.fecha_devolucion = datetime.now()  # Fecha de la devolución

    def __str__(self):
        # Mostrar la fecha de préstamo y la de devolución si ya se ha devuelto
        return f"Libro: '{self.libro.titulo}' prestado a {self.usuario.nombre} el {self.fecha_prestamo.strftime('%d/%m/%Y %H:%M:%S')} - {'Devuelto' if self.fecha_devolucion else 'Pendiente'}"
