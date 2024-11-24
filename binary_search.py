import tkinter as tk
from tkinter import messagebox

class BinarySearchDemo:
    def __init__(self, root):
        self.root = root
        self.root.title("Demostración de Búsqueda Binaria")
        
        # Crear widgets para entrada de datos
        tk.Label(root, text="Lista de números ordenados (separados por comas):").grid(row=0, column=0, padx=10, pady=5)
        self.list_entry = tk.Entry(root, width=40)
        self.list_entry.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(root, text="Número a buscar:").grid(row=1, column=0, padx=10, pady=5)
        self.target_entry = tk.Entry(root, width=20)
        self.target_entry.grid(row=1, column=1, padx=10, pady=5)
        
        # Botón para iniciar la búsqueda
        self.search_button = tk.Button(root, text="Buscar", command=self.start_search)
        self.search_button.grid(row=2, column=1, padx=10, pady=10)

        # Área de resultados de texto
        self.result_text = tk.Text(root, height=10, width=60, state="disabled")
        self.result_text.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        # Canvas para visualización gráfica
        self.canvas = tk.Canvas(root, width=1000, height=200, bg="white")
        self.canvas.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def start_search(self):
        try:
            # Leer la lista y el número objetivo
            num_list = list(map(int, self.list_entry.get().split(',')))
            target = int(self.target_entry.get())
            self.result_text.configure(state="normal")
            self.result_text.delete(1.0, tk.END)  # Limpiar resultados anteriores
            self.canvas.delete("all")  # Limpiar la visualización gráfica
            
            # Iniciar la búsqueda binaria y mostrar pasos
            index = self.binary_search(num_list, target)
            if index != -1:
                self.result_text.insert(tk.END, f"El número {target} fue encontrado en el índice {index}.\n")
            else:
                self.result_text.insert(tk.END, f"El número {target} no está en la lista.\n")
            self.result_text.configure(state="disabled")
        except ValueError:
            messagebox.showerror("Entrada inválida", "Por favor, ingrese una lista válida y un número entero.")

    def draw_array(self, num_list, low, high, mid):
        """Función para dibujar la lista y destacar los elementos actuales."""
        self.canvas.delete("all")  # Limpiar el canvas antes de dibujar
        
        # Parámetros de dibujo
        rect_width = 40
        start_x = 10
        
        for i, num in enumerate(num_list):
            x0 = start_x + i * rect_width
            x1 = x0 + rect_width
            y0, y1 = 20, 70
            
            # Colores según el estado
            if i == mid:
                color = "orange"  # Índice medio actual
            elif low <= i <= high:
                color = "lightgreen"  # Rango actual de búsqueda
            else:
                color = "lightgrey"  # Fuera del rango de búsqueda
            
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="black")
            self.canvas.create_text(x0 + rect_width / 2, (y0 + y1) / 2, text=str(num))

    def binary_search(self, num_list, target):
        low, high = 0, len(num_list) - 1
        step = 1  # Contador de pasos
        
        while low <= high:
            mid = (low + high) // 2
            self.result_text.insert(tk.END, f"Paso {step}: Buscar en índice {mid} (valor: {num_list[mid]})\n")
            self.draw_array(num_list, low, high, mid)  # Dibujar estado actual
            
            # Actualizar interfaz para mostrar paso visual
            self.canvas.update()
            self.result_text.update()
            self.root.after(1000)  # Pausa de 1 segundo entre pasos
            
            step += 1
            
            if num_list[mid] == target:
                return mid
            elif num_list[mid] < target:
                low = mid + 1
                self.result_text.insert(tk.END, f"   El valor {target} es mayor que {num_list[mid]}, buscar a la derecha.\n")
            else:
                high = mid - 1
                self.result_text.insert(tk.END, f"   El valor {target} es menor que {num_list[mid]}, buscar a la izquierda.\n")
        
        return -1


def main():
    # Crear la ventana principal de Tkinter
    root = tk.Tk()
    app = BinarySearchDemo(root)
    root.mainloop()

# Ejecutar el código solo si es el archivo principal
if __name__ == "__main__":
    main()
