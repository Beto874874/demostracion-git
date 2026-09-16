def calculadora():
    while True:
        print("Seleccione una operación:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = input("Ingrese el número de la operación que desea realizar: ")

        if opcion == '5':
            print("Saliendo de la calculadora.")
            break

        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == '1':
            resultado = num1 + num2
            print(f"El resultado de la suma es: {resultado}")
        elif opcion == '2':
            resultado = num1 - num2
            print(f"El resultado de la resta es: {resultado}")
        elif opcion == '3':
            resultado = num1 * num2
            print(f"El resultado de la multiplicación es: {resultado}")
        elif opcion == '4':
            if num2 != 0:
                resultado = num1 / num2
                print(f"El resultado de la división es: {resultado}")
            else:
                print("Error: No se puede dividir entre cero.")
        else:
            print("Opción no válida. Por favor, intente nuevamente.")