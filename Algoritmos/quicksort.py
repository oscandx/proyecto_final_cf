import tkinter as tk
import random
import time
from decorators import timing_decorator
from typing import List, Optional


class QuickSortVisualizer:
    """Clase que contiene los atributos y métodos de ejecución necesarios del algoritmo quicksort."""
    def __init__(self, root):
        self.root = root
        self.root.title("Demostración de Quicksort")

        # configuración de la interfaz
        tk.Label(root, text="Número de elementos:").pack()
        self.num_elements_entry = tk.Entry(root)
        self.num_elements_entry.pack()

        self.start_button = tk.Button(root, text="Iniciar Quicksort", command=self.start_sort)
        self.start_button.pack()

        # slider para controlar la velocidad
        tk.Label(root, text="Velocidad de visualización (ms):").pack()
        self.speed_slider = tk.Scale(root, from_=10, to=1000, orient=tk.HORIZONTAL)
        self.speed_slider.set(500)  # velocidad inicial (500 ms)
        self.speed_slider.pack()

        # se usa canvas para la visualización
        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack()

        # datos iniciales
        self.data = []

    def start_sort(self):
        # se obtener el número de elementos y generar datos aleatorios
        num_elements = int(self.num_elements_entry.get())
        self.data = [random.randint(5, 400) for _ in range(num_elements)]
        
        # se dibujan los datos iniciales en el canvas
        self.draw_data(self.data, ['blue' for _ in range(len(self.data))])
        
        # se ejecuta Quicksort y se visualiza el proceso
        self.quick_sort(0, len(self.data) - 1)

    def draw_data(self, data, color_array):
        """Dibuja los elementos en el canvas con colores específicos para cada elemento."""
        self.canvas.delete("all")
        canvas_height = 400
        canvas_width = 600
        bar_width = canvas_width / (len(data) + 1)
        offset = 30
        spacing = 10

        for i, height in enumerate(data):
            # coordenadas de cada barra
            x0 = i * bar_width + offset + spacing
            y0 = canvas_height - height
            x1 = (i + 1) * bar_width + offset
            y1 = canvas_height

            # se dibuja cada barra
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])
            self.canvas.create_text(x0 + 2, y0, anchor=tk.SW, text=str(data[i]))

        self.root.update_idletasks()
        time.sleep(self.speed_slider.get() / 1000)  # pausa ajustable según el slider

    @timing_decorator
    def quick_sort(self, low, high):
        """Función principal de Quicksort con visualización."""
        if low < high:
            # se obtiene el índice de partición
            pivot_index = self.partition(low, high)
            
            # se ordenan las dos mitades
            self.quick_sort(low, pivot_index - 1)
            self.quick_sort(pivot_index + 1, high)

    def partition(self, low, high):
        """Función de partición que ordena los elementos alrededor del pivote."""
        pivot = self.data[high]
        i = low - 1

        for j in range(low, high):
            if self.data[j] <= pivot:
                i += 1
                self.data[i], self.data[j] = self.data[j], self.data[i]
                self.draw_data(self.data, ['green' if x == i or x == j else 'blue' for x in range(len(self.data))])

        # se coloca el pivote en la posición correcta
        self.data[i + 1], self.data[high] = self.data[high], self.data[i + 1]
        self.draw_data(self.data, ['purple' if x == i + 1 else 'blue' for x in range(len(self.data))])
        
        return i + 1


def quicksort_f(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort_f(left) + middle + quicksort_f(right)

def main():
    # se crea la ventana principal de Tkinter
    root = tk.Tk()
    app = QuickSortVisualizer(root)
    root.mainloop()

# ejecución del código
if __name__ == "__main__":
    main()