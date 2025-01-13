# Clase Libro
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True  # El libro está disponible por defecto

    def __str__(self):
        return f"'{self.titulo}' de {self.autor} - {'Disponible' if self.disponible else 'Prestado'}"