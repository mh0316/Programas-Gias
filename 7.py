def es_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    else:
        i = 5
        while i * i <= numero:
            if numero % i == 0 or numero % (i + 2) == 0:
                return False
            i += 6
        return True

def calcular_modulo_primos(primo1, primo2):
    if not es_primo(primo1) or not es_primo(primo2):
        raise ValueError("Ambos números deben ser primos")
    return primo1 % primo2

def main():
    primo1 = int(input("Ingrese el primer número primo: "))
    primo2 = int(input("Ingrese el segundo número primo: "))

    try:
        resultado = calcular_modulo_primos(primo1, primo2)
        print(f"{primo1} mod {primo2} es: {resultado}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()