# Pruebas unitarias del sistema
import unittest
from clases.libros import Libro
from clases.usuarios import Usuario


class TestSistemaBiblioteca(unittest.TestCase):

    def test_creacion_libro(self):
        libro = Libro("1984", "George Orwell")
        self.assertEqual(libro.titulo, "1984")
        self.assertEqual(libro.autor, "George Orwell")

    def test_creacion_usuario(self):
        usuario = Usuario("Juan Perez", 12345678)
        self.assertEqual(usuario.nombre, "Juan Perez")
        self.assertEqual(usuario.dni, 12345678)


if __name__ == "__main__":
    unittest.main()
