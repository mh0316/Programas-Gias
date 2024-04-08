def euclides_extendido(a, b):
    if a == 0:
        return b, 0, 1
    else:
        mcd, x, y = euclides_extendido(b % a, a)
        return mcd, y - (b // a) * x, x

def inverso_modular(a, m):
    mcd, x, y = euclides_extendido(a, m)
    if mcd != 1:
        raise ValueError("El inverso modular no existe")
    else:
        return x % m

def main():
    a = int(input("Ingrese el número primo a: "))
    m = int(input("Ingrese el número grande m: "))

    try:
        inverso = inverso_modular(a, m)
        print("El inverso modular de", a, "módulo", m, "es:", inverso)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()