def producto_horas_modular(hora1, hora2):
    # Calcula el producto de dos horas del día en formato de 24 horas de forma modular, donde el módulo es 24.
    # Calcula el producto y aplica la operación de módulo 24
    producto = (hora1 * hora2) % 24
    return producto

# Ejemplo de uso
hora1 = 10
hora2 = 15
resultado = producto_horas_modular(hora1, hora2)
print("El producto de las horas de forma modular es: ", resultado)