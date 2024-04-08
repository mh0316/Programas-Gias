def exponenciacion_rapida(a, b, m):
    # Calcula a^b mod m utilizando el método de exponenciación rápida.
    resultado = 1
    a = a % m  # Se toma el módulo de a para evitar posibles desbordamientos

    while b > 0:
        # Si b es impar, multiplicamos result por a
        if b % 2 == 1:
            resultado = (resultado * a) % m

        # Dividimos b por 2 y tomamos el residuo
        b //= 2

        # Elevamos a al cuadrado
        a = (a * a) % m

    return resultado

a = 7
b = 13
m = 10
resultado = exponenciacion_rapida(a, b, m)
print(f"{a}^{b} mod {m} = {resultado}")