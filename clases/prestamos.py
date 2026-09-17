from datetime import datetime, timedelta

# Clase Prestamo
class Prestamo:
    DIAS_PRESTAMO = 7  # Plazo estándar de préstamo en días

    def __init__(self, usuario, libro):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = datetime.now()
        self.fecha_limite = self.fecha_prestamo + timedelta(days=self.DIAS_PRESTAMO)
        self.fecha_devolucion = None

    def devolver_libro(self):
        self.fecha_devolucion = datetime.now()

    #verificar si se encuentra atrazado en la devolucion
    def esta_atrasado(self):
        fecha_referencia = self.fecha_devolucion or datetime.now()
        return fecha_referencia > self.fecha_limite
    
    def __str__(self):
        return f"Libro: '{self.libro.titulo}' prestado a {self.usuario.nombre} el {self.fecha_prestamo.strftime('%d/%m/%Y %H:%M:%S')} - {'Devuelto' if self.fecha_devolucion else 'Pendiente'}"