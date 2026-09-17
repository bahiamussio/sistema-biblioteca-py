from clases.libros import Libro
from clases.prestamos import Prestamo
from clases.usuarios import Usuario
from biblioteca import Biblioteca


# Función del menú interactivo
def mostrar_menu():
    biblioteca = Biblioteca()  # Crear una instancia de la biblioteca

    while True:
        print("\n--- Menú de la Biblioteca de Haku ---")
        print("1. Registrar libro 📚")
        print("2. Registrar usuario 👤")
        print("3. Ver libros disponibles 📖")
        print("4. Prestar libro 📘")
        print("5. Devolver libro 🔄")
        print("6. Ver lista de libros prestados 📝")
        print("7. Ver lista de usuarios registrados 🧑‍🤝‍🧑")
        print("8. Eliminar libro 🗑️")
        print("9. Salir ❌")

        opcion = input(
            "¡Bienvenido a la Biblioteca de Haku! Por favor, elige una opción: "
        )

        if opcion == "1":
            titulo = input("Ingresa el título del libro: ")
            autor = input("Ingresa el autor del libro: ")
            biblioteca.registrar_libro(titulo, autor)

        elif opcion == "2":
            nombre = input("Ingresa el nombre del usuario: ")
            dni = int(input("Ingresa el DNI del usuario: "))
            biblioteca.registrar_usuario(nombre, dni)

        elif opcion == "3":
            biblioteca.mostrar_libros()

        elif opcion == "4":
            dni = int(input("Ingresa el DNI del usuario: "))
            titulo = input("Ingresa el título del libro: ")
            biblioteca.prestar_libro(dni, titulo)

        elif opcion == "5":
            dni = int(input("Ingresa el DNI del usuario: "))
            titulo = input("Ingresa el título del libro: ")
            biblioteca.devolver_libro(dni, titulo)

        elif opcion == "6":
            biblioteca.mostrar_usuarios_prestados()

        elif opcion == "7":
            biblioteca.mostrar_usuarios()

        elif opcion == "8":
            titulo = input("Ingresa el título del libro que deseas eliminar: ")
            biblioteca.eliminar_libro(titulo)

        elif opcion == "9":
            print("¡Gracias por usar el sistema de la Biblioteca de Haku!")
            break

        else:
            print("Opción no válida. Por favor, elige una opción correcta.")


# Llamar a la función menu para que el programa empiece
if __name__ == "__main__":
    mostrar_menu()