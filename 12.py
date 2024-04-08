import tkinter as tk
from tkinter import messagebox

class AlgoritmoCambioDeBase:
    def __init__(self, numero, primera_base, segunda_base):
        self.numero = numero
        self.primera_base = primera_base
        self.segunda_base = segunda_base

    def convertir_base_primera_base(self):
        numero_base_10 = self.convertir_a_base_10()
        resultado = ""
        while numero_base_10 != 0:
            digito = numero_base_10 % self.primera_base
            caracter = str(digito) if digito < 10 else chr(digito - 10 + ord('A'))
            resultado = caracter + resultado
            numero_base_10 //= self.primera_base
        return resultado

    def convertir_base_segunda_base(self):
        numero_base_10 = self.convertir_a_base_10()
        resultado = ""
        while numero_base_10 != 0:
            digito = numero_base_10 % self.segunda_base
            caracter = str(digito) if digito < 10 else chr(digito - 10 + ord('A'))
            resultado = caracter + resultado
            numero_base_10 //= self.segunda_base
        return resultado

    def convertir_a_base_10(self):
        numero_original = self.numero
        numero_base_10 = 0
        potencia = 0
        while numero_original != 0:
            digito = numero_original % 10
            numero_base_10 += digito * (self.primera_base ** potencia)
            numero_original //= 10
            potencia += 1
        return numero_base_10

class Ventana:
    def __init__(self, root):
        self.root = root
        self.root.title("Cambio de Base")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.etiqueta_pedir_numero = tk.Label(root, text="Ingrese un número:")
        self.etiqueta_pedir_numero.place(x=20, y=30)

        self.etiqueta_pedir_bases = tk.Label(root, text="Ingrese las bases:")
        self.etiqueta_pedir_bases.place(x=20, y=90)

        self.etiqueta_resultados = tk.Label(root, text="Resultados:")
        self.etiqueta_resultados.place(x=250, y=30)

        self.etiqueta_primera_base = tk.Label(root, text="")
        self.etiqueta_primera_base.place(x=250, y=60)

        self.etiqueta_segunda_base = tk.Label(root, text="")
        self.etiqueta_segunda_base.place(x=250, y=90)

        self.caja_ingreso_numero = tk.Entry(root)
        self.caja_ingreso_numero.place(x=20, y=60)

        self.caja_primera_base = tk.Entry(root)
        self.caja_primera_base.place(x=20, y=120)

        self.caja_segunda_base = tk.Entry(root)
        self.caja_segunda_base.place(x=20, y=140)

        self.boton_cambio_de_base = tk.Button(root, text="Cambiar Base", command=self.cambiar_base)
        self.boton_cambio_de_base.place(x=150, y=180)

        self.boton_limpiar = tk.Button(root, text="Limpiar", command=self.limpiar)
        self.boton_limpiar.place(x=160, y=220)

    def cambiar_base(self):
        try:
            numero = int(self.caja_ingreso_numero.get())
            primera_base = int(self.caja_primera_base.get())
            segunda_base = int(self.caja_segunda_base.get())

            algoritmo = AlgoritmoCambioDeBase(numero, primera_base, segunda_base)
            resultado_primera = algoritmo.convertir_base_primera_base()
            resultado_segunda = algoritmo.convertir_base_segunda_base()

            self.etiqueta_primera_base.config(text=f"Base {primera_base}: {resultado_primera}")
            self.etiqueta_segunda_base.config(text=f"Base {segunda_base}: {resultado_segunda}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese números válidos")

    def limpiar(self):
        self.caja_ingreso_numero.delete(0, tk.END)
        self.caja_primera_base.delete(0, tk.END)
        self.caja_segunda_base.delete(0, tk.END)
        self.etiqueta_primera_base.config(text="")
        self.etiqueta_segunda_base.config(text="")

def main():
    root = tk.Tk()
    ventana = Ventana(root)
    root.mainloop()

if __name__ == "__main__":
    main()