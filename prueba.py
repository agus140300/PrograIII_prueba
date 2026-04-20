def SumarNumero(a, b):
    return a + b
if __name__ == "__main__":
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    resultado = SumarNumero(a, b)
    print(f"La suma de {a} y {b} es: {resultado}")
    