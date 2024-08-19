def sumar(a,b):
    return a + b

def restar(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    if b == 0:
        return "error: División por cero"
    else:
        return a/b

if __name__ == "__main__":
    print("Calculadora simple")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = int(input("Elige una opción (1/2/3/4): "))
    num1 = float(input("Introduce el primer número"))
    num2 = float(input("Introduce el segundo número"))

    if opcion == 1:
        print(f"Resultado: {sumar(num1, num2)}")
    elif opcion == 2:
        print(f"Resultado: {restar(num1, num2)}")
    elif opcion == 3:
        print(f"Resultado: {multiplicar(num1, num2)}")
    elif opcion == 4:
        print(f"Resultado: {dividir(num1, num2)}")
    else:
        print("Opción no válida")
