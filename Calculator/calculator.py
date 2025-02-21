# Funciones para las operaciones
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero"

# Función para mostrar el menú
def mostrar_menu():
    print("Seleccione una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

# Función principal
def calculadora():
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la operación que desea realizar: ")

        if opcion == '5':
            print("Gracias por usar la calculadora.")
            break

        if opcion in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
            except ValueError:
                print("Error: Debe ingresar números válidos.")
                continue

            if opcion == '1':
                print(f"El resultado es: {suma(num1, num2)}")
            elif opcion == '2':
                print(f"El resultado es: {resta(num1, num2)}")
            elif opcion == '3':
                print(f"El resultado es: {multiplicacion(num1, num2)}")
            elif opcion == '4':
                print(f"El resultado es: {division(num1, num2)}")
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

# Ejecutar la calculadora
calculadora()
