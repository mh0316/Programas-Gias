def mcd_extendido(a, b):
    # Calcula el máximo común divisor (M.C.D.) de dos números y sus coeficientes bezout.
    if a == 0:
        return b, 0, 1
    mcd, x1, y1 = mcd_extendido(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return mcd, x, y

def inverso_modular(a, m):
    # Calcula el inverso modular de a en m utilizando el algoritmo de Euclides extendido.
    mcd, x, y = mcd_extendido(a, m)
    if mcd != 1:
        raise ValueError(f"{a} no es invertible en modulo {m}")
    return (x % m + m) % m

def resolver_sistema_lineal(coeficientes, mod):
    # Resuelve un sistema de ecuaciones lineales utilizando aritmética modular.
    n = len(coeficientes)

    # Convertir el sistema de ecuaciones a triangular superior
    for i in range(n):
        for j in range(i+1, n):
            # Encontrar el múltiplo para hacer 0 el coeficiente en la columna i
            # y ajustar los otros coeficientes
            mul = (coeficientes[j][i] * inverso_modular(coeficientes[i][i], mod)) % mod
            coeficientes[j] = [(coeficientes[j][k] - mul * coeficientes[i][k]) % mod for k in range(n+1)]

    # Resolución hacia atrás
    solution = [0] * n
    for i in range(n-1, -1, -1):
        temp_solution = solution[:]  # Crear una copia temporal de la solución
        solution[i] = coeficientes[i][n]
        for j in range(i+1, n):
            solution[i] = (solution[i] - coeficientes[i][j] * temp_solution[j]) % mod
        solution[i] = (solution[i] * inverso_modular(coeficientes[i][i], mod)) % mod

    return tuple(solution)

# Ejemplo de uso
coefficients = [(2, 3, 5), (3, 5, 8)]  # Representa el sistema de ecuaciones 2x + 3y = 5 y 3x + 5y = 8
mod = 11  # El módulo
solucion = resolver_sistema_lineal(coefficients, mod)
print("Solución del sistema de ecuaciones:", solucion)