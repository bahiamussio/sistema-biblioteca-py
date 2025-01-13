# Sistema de Gestión de Biblioteca - Biblioteca de Haku

Este proyecto es un sistema interactivo para la gestión de una biblioteca, implementado en Python utilizando principios de Programación Orientada a Objetos (POO). El sistema permite realizar operaciones como registrar libros y usuarios, prestar y devolver libros, y visualizar información relacionada con la biblioteca.

---

## Funcionalidades

1. **Registrar libros** 📚  
   Permite agregar nuevos libros a la biblioteca con su título y autor.

2. **Registrar usuarios** 👤  
   Añade usuarios al sistema mediante su nombre y DNI.

3. **Ver libros disponibles** 📖  
   Muestra una lista de libros que aún no han sido prestados.

4. **Prestar libros** 📘  
   Asocia un libro disponible a un usuario registrado, marcándolo como prestado.

5. **Devolver libros** 🔄  
   Permite a un usuario registrado devolver un libro previamente prestado, actualizando su estado a disponible.

6. **Ver lista de libros prestados** 📝  
   Presenta una lista de los libros que han sido prestados, junto con el nombre del usuario que los tomó.

7. **Ver lista de usuarios registrados** 🧑‍🤝‍🧑  
   Muestra todos los usuarios registrados en el sistema.

8. **Salir del programa** ❌  
   Finaliza la ejecución del sistema.

---

## Estructura del Proyecto

El proyecto está organizado en módulos y clases para facilitar su mantenimiento y ampliación:

- **`clases/`**: Contiene las clases principales:
  - `Libro`: Representa los libros de la biblioteca.
  - `Usuario`: Representa a los usuarios registrados.
  - `Prestamo`: Maneja la relación entre un usuario y un libro prestado.

- **`biblioteca.py`**: Clase principal `Biblioteca`, que centraliza todas las operaciones del sistema.

- **`main.py`**: Archivo ejecutable que implementa un menú interactivo para interactuar con el sistema.

---

## Requisitos

- Python 3.8 o superior

---

## Contribuciones

¡Toda colaboración es bienvenida! Si tienes ideas o mejoras, no dudes en abrir un issue o enviar un pull request.

---

## Autoría
Este proyecto fue desarrollado como parte de un aprendizaje práctico en POO con Python.
Inspirado por Haku, la mejor compañera felina. 🐾
