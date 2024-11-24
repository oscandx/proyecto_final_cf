import tkinter as tk
import random
import time
from decorators import timing_decorator

class QuickSortVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Demostración de Quicksort")

        # Configuración de la interfaz
        tk.Label(root, text="Número de elementos:").pack()
        self.num_elements_entry = tk.Entry(root)
        self.num_elements_entry.pack()

        self.start_button = tk.Button(root, text="Iniciar Quicksort", command=self.start_sort)
        self.start_button.pack()

        # Slider para controlar la velocidad
        tk.Label(root, text="Velocidad de visualización (ms):").pack()
        self.speed_slider = tk.Scale(root, from_=10, to=1000, orient=tk.HORIZONTAL)
        self.speed_slider.set(500)  # Velocidad inicial (500 ms)
        self.speed_slider.pack()

        # Canvas para visualización
        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack()

        # Datos iniciales
        self.data = []

    def start_sort(self):
        # Obtener el número de elementos y generar datos aleatorios
        num_elements = int(self.num_elements_entry.get())
        self.data = [random.randint(5, 400) for _ in range(num_elements)]
        
        # Dibujar datos iniciales en el canvas
        self.draw_data(self.data, ['blue' for _ in range(len(self.data))])
        
        # Ejecutar Quicksort y visualizar el proceso
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
            # Coordenadas de cada barra
            x0 = i * bar_width + offset + spacing
            y0 = canvas_height - height
            x1 = (i + 1) * bar_width + offset
            y1 = canvas_height

            # Dibujar cada barra
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])
            self.canvas.create_text(x0 + 2, y0, anchor=tk.SW, text=str(data[i]))

        self.root.update_idletasks()
        time.sleep(self.speed_slider.get() / 1000)  # Pausa ajustable según el slider

    @timing_decorator
    def quick_sort(self, low, high):
        """Función principal de Quicksort con visualización."""
        if low < high:
            # Obtener el índice de partición
            pivot_index = self.partition(low, high)
            
            # Ordenar las dos mitades
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

        # Colocar el pivote en la posición correcta
        self.data[i + 1], self.data[high] = self.data[high], self.data[i + 1]
        self.draw_data(self.data, ['purple' if x == i + 1 else 'blue' for x in range(len(self.data))])
        
        return i + 1

def main():
    # Crear la ventana principal de Tkinter
    root = tk.Tk()
    app = QuickSortVisualizer(root)
    root.mainloop()

# Ejecutar el código solo si es el archivo principal
if __name__ == "__main__":
    main()