import tkinter as tk
from tkinter import messagebox


class RecursionStackDemo:
    """Clase que contiene los atributos y métodos de ejecución necesarios del algoritmo de recursión."""
    def __init__(self, root):
        self.root = root
        self.root.title("Demostración de Recursión con Pila de Llamadas (Factorial)")

        # se crean los widgets para la entrada de datos
        tk.Label(root, text="Número para calcular factorial:").grid(row=0, column=0, padx=10, pady=5)
        self.num_entry = tk.Entry(root, width=20)
        self.num_entry.grid(row=0, column=1, padx=10, pady=5)

        # se crea el botón para iniciar el cálculo de factorial
        self.calculate_button = tk.Button(root, text="Calcular", command=self.start_calculation)
        self.calculate_button.grid(row=1, column=1, padx=10, pady=10)

        # área de resultados de texto
        self.result_text = tk.Text(root, height=10, width=50, state="disabled")
        self.result_text.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        # canvas para visualización gráfica de la pila
        self.canvas = tk.Canvas(root, width=400, height=300, bg="white")
        self.canvas.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def start_calculation(self):
        try:
            # se lee el número ingresado por el usuario
            number = int(self.num_entry.get())
            if number < 0:
                raise ValueError("El número debe ser no negativo.")

            self.result_text.configure(state="normal")
            self.result_text.delete(1.0, tk.END)  # se limpian resultados anteriores
            self.canvas.delete("all")  # se limpia la visualización de la pila

            # cálculo de factorial y mostrar pasos
            result = self.calculate_factorial(number, 0)
            self.result_text.insert(tk.END, f"\nEl factorial de {number} es: {result}\n")
            self.result_text.configure(state="disabled")
        except ValueError:
            messagebox.showerror("Entrada inválida", "Por favor, ingrese un número entero no negativo.")

    def calculate_factorial(self, n, depth):
        """Función recursiva para calcular el factorial y mostrar la pila de llamadas."""
        # se muestra la llamada actual en la pila, desde abajo hacia arriba
        self.push_stack(f"factorial({n})", depth)

        if n == 0 or n == 1:
            self.result_text.insert(tk.END, f"factorial({n}) = 1 (caso base)\n")
            self.result_text.update()
            self.root.after(500)  # pausa de 0.5 segundos
            self.pop_stack(depth)
            return 1
        else:
            self.result_text.insert(tk.END, f"factorial({n}) = {n} * factorial({n-1})\n")
            self.result_text.update()
            self.root.after(1000)  # pausa de 1 segundo

            # llamada recursiva
            result = n * self.calculate_factorial(n - 1, depth + 1)

            # se muestra el resultado al regresar de la llamada recursiva
            self.result_text.insert(tk.END, f"Retornando: {n} * factorial({n-1}) = {result}\n")
            self.result_text.update()
            self.root.after(500)  # pausa de 0.5 segundos
            self.pop_stack(depth)
            return result

    def push_stack(self, text, depth):
        """Agregar una llamada a la pila visual en el canvas desde la parte inferior."""
        x, y = 200, 250 - depth * 30  # comienza desde la parte inferior (y=250)
        rect_id = self.canvas.create_rectangle(x - 50, y - 15, x + 50, y + 15, fill="lightblue", outline="black")
        text_id = self.canvas.create_text(x, y, text=text)
        self.canvas.update()
        self.root.after(500)  # pausa para ver cómo se agrega la llamada a la pila
        return rect_id, text_id

    def pop_stack(self, depth):
        """Eliminar la última llamada de la pila visual en el canvas desde la parte superior."""
        x, y = 200, 250 - depth * 30  # empieza a eliminar desde la parte superior
        for item in self.canvas.find_overlapping(x - 50, y - 15, x + 50, y + 15):
            self.canvas.delete(item)
        self.canvas.update()
        self.root.after(500)  # pausa para ver cómo se elimina la llamada de la pila


def main():
    # se crea la ventana principal de Tkinter
    root = tk.Tk()
    app = RecursionStackDemo(root)
    root.mainloop()

# ejecución del código
if __name__ == "__main__":
    main()