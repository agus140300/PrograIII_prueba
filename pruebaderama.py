def pedirnumero():
    while True:
        try:
            numero = int(input("Ingrese un número entero: "))
            return numero
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")1
if __name__ == "__main__":
    numero1 = pedirnumero()
    numero2 = pedirnumero()
    print(f"El número ingresado es: {numero1}")
    print(f"El número ingresado es: {numero2}")