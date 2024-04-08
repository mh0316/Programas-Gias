import random

def generar_matriz(filas, columnas, min_valor, max_valor):
    matriz = []
    for _ in range(filas):
        fila = [round(random.uniform(min_valor, max_valor), 2) for _ in range(columnas)]
        matriz.append(fila)
    return matriz

def decimal_a_binario(numero):
    parte_entera = int(numero)
    parte_decimal = numero - parte_entera
    parte_decimal_binaria = ""
    for _ in range(2):  # Limitamos a dos decimales
        parte_decimal *= 2
        if parte_decimal >= 1:
            parte_decimal_binaria += "1"
            parte_decimal -= 1
        else:
            parte_decimal_binaria += "0"
    return f"{parte_entera:b}.{parte_decimal_binaria}"

def matriz_decimal_a_binario(matriz):
    matriz_binaria = []
    for fila in matriz:
        fila_binaria = [decimal_a_binario(num) for num in fila]
        matriz_binaria.append(fila_binaria)
    return matriz_binaria

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

def main():
    filas = int(input("Ingrese el número de filas de la matriz: "))
    columnas = int(input("Ingrese el número de columnas de la matriz: "))
    min_valor = float(input("Ingrese el valor mínimo para los números aleatorios: "))
    max_valor = float(input("Ingrese el valor máximo para los números aleatorios: "))

    matriz_decimal = generar_matriz(filas, columnas, min_valor, max_valor)
    print("Matriz en números decimales:")
    imprimir_matriz(matriz_decimal)

    matriz_binaria = matriz_decimal_a_binario(matriz_decimal)
    print("\nMatriz en números binarios:")
    imprimir_matriz(matriz_binaria)

if __name__ == "__main__":
    main()