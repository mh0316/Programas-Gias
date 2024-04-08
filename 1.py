import random

def miller_rabin(n, k=5):
    """
    Test de primalidad de Miller-Rabin.
    
    Args:
        n (int): Número a verificar si es primo.
        k (int): Número de iteraciones. Cuanto mayor sea k, mayor será la confianza en el resultado.
        
    Returns:
        bool: True si el número es probablemente primo, False si es compuesto.
    """
    # Casos especiales
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Escribir n-1 como 2^s * d
    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    # Realizar el test k veces
    for _ in range(k):
        a = random.randint(2, n - 1)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

numero = int(input("Ingrese un número: "))

if miller_rabin(numero):
    print(f"{numero} es probablemente primo.")
else:
    print(f"{numero} es compuesto.")