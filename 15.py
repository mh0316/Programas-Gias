from itertools import product

def generar_codigos_barras(simbolos, longitud):
    return [''.join(codigo) for codigo in product(simbolos, repeat=longitud)]

def main():
    simbolos = ['0', '1', '2', '3']  # Puedes cambiar estos símbolos según sea necesario
    longitud_codigo = 12

    codigos_barras = generar_codigos_barras(simbolos, longitud_codigo)

    print("Códigos de barras generados:")
    for codigo in codigos_barras:
        print(codigo)

if __name__ == "__main__":
    main()