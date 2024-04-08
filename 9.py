def factorizar_numero(numero):
    factores_primos = []
    divisor = 2
    while numero > 1:
        while numero % divisor == 0:
            factores_primos.append(divisor)
            numero //= divisor
        divisor += 1
    return factores_primos

def main():
    numero = int(input("Ingrese un número para factorizar: "))
    factores_primos = factorizar_numero(numero)
    print("Los factores primos de", numero, "son:", factores_primos)

if __name__ == "__main__":
    main()