def calcular_mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def son_coprimos(a, b):
    return calcular_mcd(a, b) == 1

def main():
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))

    if son_coprimos(numero1, numero2):
        print(f"{numero1} y {numero2} son coprimos.")
    else:
        print(f"{numero1} y {numero2} no son coprimos.")

if __name__ == "__main__":
    main()