def suma_fechas_modular(fecha1, fecha2):
    # Calcula la suma de dos fechas de forma modular, donde el módulo representa el número de días en una semana (7 días).
    # Suma las fechas y aplica la suma modular de 7
    suma = (fecha1 + fecha2) % 7
    # Ajusta para que lunes sea el primer día de la semana (0)
    return (suma - 1) % 7

# Ejemplo de uso
fecha1 = 15
fecha2 = 6
resultado = suma_fechas_modular(fecha1, fecha2)
print("La suma de las fechas de forma modular (considerando lunes como el primer día de la semana) es: ", resultado)