def calculadora():
    print("Calculadora Básica - Operaciones: suma, resta, multiplicación, división")
    print("Escribe la operación completa (ejemplo: 2 + 2) y presiona Enter para calcular.")
    print("Presiona 'c' para borrar la entrada y comenzar de nuevo.")
    print("Presiona 'q' para salir.")

    while True:
        # Leer la entrada del usuario
        entrada = input("Introduce una operación: ")

        # Manejar la salida
        if entrada.lower() == 'q':
            print("Saliendo de la calculadora.")
            break

        # Manejar el borrado de la entrada
        if entrada.lower() == 'c':
            print("Entrada borrada.")
            continue

        try:
            # Evaluar la operación y mostrar el resultado
            resultado = eval(entrada)
            print(f"Resultado: {resultado}")
        except Exception as e:
            # Manejar errores en la evaluación de la operación
            print(f"Error: {e}. Asegúrate de que la operación es válida.")

if __name__ == "__main__":
    calculadora()
