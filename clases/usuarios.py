# Clase Usuario
class Usuario:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
        self.prestamos = []  # Lista para los préstamos realizados por el usuario

    def __str__(self):
        return f"{self.nombre} (DNI: {self.dni})"