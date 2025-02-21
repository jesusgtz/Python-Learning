#Funciones para la conversion
def celsius(f):
    return (((f-32)*5)/9)

def fahrenheit(c):
    return (c*(9/5))+32

#Funcion para mostrar el menu
def mostrar_menu():
    print("Selecciona una conversion:")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Salir")

#Funcion principal
def conversor():
    while True:
        mostrar_menu()
        opcion = input("Ingrese el numero de la operacion que desea realizar: ")

        if opcion == '3':
            print("Gracias por usar el conversor")
            break

        if opcion in ['1', '2']:
            if opcion == '1':
                c = float(input("Ingrese el valor de grados Celsius: "))
                print(f"El resultado es {fahrenheit(c)}  grados Fahrenheit")
            elif opcion == '2':
                f = float(input("Ingrese el valor de grados Fahrenheit: "))
                print(f"El resultado es {celsius(f)} grados Celsius")
        else:
            print("Opción no valida. Por favor, selecciona una opcion valida")

#Ejecutar el conversor
conversor()
