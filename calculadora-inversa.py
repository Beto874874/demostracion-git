def calculadora_inversa(a,b):
    while True:
        print("Seleccione una operación:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = input("Ingrese el número de la operación que desea realizar: ")

        if opcion == '5':
            print("Saliendo de la calculadora inversa.")
            break

        if opcion == '1':
            resultado = a + b
            print(f"El resultado de la suma es: {resultado}")
        elif opcion == '2':
            resultado = a - b
            print(f"El resultado de la resta es: {resultado}")
        elif opcion == '3':
            resultado = a * b
            print(f"El resultado de la multiplicación es: {resultado}")
        elif opcion == '4':
            if b != 0:
                resultado = a / b
                print(f"El resultado de la división es: {resultado}")
            else:
                print("Error: No se puede dividir entre cero.")
        else:
            print("Opción no válida. Por favor, intente nuevamente.")