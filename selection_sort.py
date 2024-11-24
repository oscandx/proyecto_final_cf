import tkinter as tk
from tkinter import messagebox


class SelectionSortDemo:
    def __init__(self, root):
        self.root = root
        self.root.title("Demostración de Ordenamiento por Selección")
        
        # Crear widgets para entrada de datos
        tk.Label(root, text="Lista de números (separados por comas):").grid(row=0, column=0, padx=10, pady=5)
        self.list_entry = tk.Entry(root, width=40)
        self.list_entry.grid(row=0, column=1, padx=10, pady=5)
        
        # Botón para iniciar el ordenamiento
        self.sort_button = tk.Button(root, text="Ordenar", command=self.start_sorting)
        self.sort_button.grid(row=1, column=1, padx=10, pady=10)

        # Área de resultados de texto
        self.result_text = tk.Text(root, height=10, width=60, state="disabled")
        self.result_text.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        # Canvas para visualización gráfica
        self.canvas = tk.Canvas(root, width=500, height=100, bg="white")
        self.canvas.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def start_sorting(self):
        try:
            # Leer la lista y convertirla en una lista de enteros
            num_list = list(map(int, self.list_entry.get().split(',')))
            self.result_text.configure(state="normal")
            self.result_text.delete(1.0, tk.END)  # Limpiar resultados anteriores
            self.canvas.delete("all")  # Limpiar la visualización gráfica
            
            # Iniciar el ordenamiento por selección y mostrar pasos
            self.selection_sort(num_list)
            self.result_text.insert(tk.END, f"Lista ordenada: {num_list}\n")
            self.result_text.configure(state="disabled")
        except ValueError:
            messagebox.showerror("Entrada inválida", "Por favor, ingrese una lista válida de números enteros.")

    def draw_array(self, num_list, current_index, min_index):
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
            if i == min_index:
                color = "orange"  # Índice del mínimo actual
            elif i == current_index:
                color = "lightblue"  # Índice actual a comparar
            else:
                color = "lightgrey"  # Otros elementos
            
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="black")
            self.canvas.create_text(x0 + rect_width / 2, (y0 + y1) / 2, text=str(num))

    def selection_sort(self, num_list):
        n = len(num_list)
        for i in range(n - 1):
            min_index = i
            self.result_text.insert(tk.END, f"Paso {i + 1}: buscar mínimo desde índice {i}\n")
            
            for j in range(i + 1, n):
                self.draw_array(num_list, j, min_index)  # Dibujar estado actual
                
                # Actualizar interfaz para mostrar paso visual
                self.canvas.update()
                self.result_text.update()
                self.root.after(500)  # Pausa de 0.5 segundos entre comparaciones
                
                if num_list[j] < num_list[min_index]:
                    min_index = j
                    self.result_text.insert(tk.END, f"   Nuevo mínimo encontrado en índice {min_index} (valor: {num_list[min_index]})\n")
                    self.draw_array(num_list, j, min_index)  # Actualizar con nuevo mínimo encontrado
                    
            # Intercambiar el mínimo con el elemento en la posición i
            num_list[i], num_list[min_index] = num_list[min_index], num_list[i]
            self.result_text.insert(tk.END, f"Intercambiar índice {i} con índice {min_index}\n")
            self.draw_array(num_list, i, min_index)  # Dibujar intercambio
            
            # Pausa para mostrar el intercambio
            self.canvas.update()
            self.root.after(1000)  # Pausa de 1 segundo antes del próximo paso

def main():
    # Crear la ventana principal de Tkinter
    root = tk.Tk()
    app = SelectionSortDemo(root)
    root.mainloop()

# Ejecutar el código solo si es el archivo principal
if __name__ == "__main__":
    main()