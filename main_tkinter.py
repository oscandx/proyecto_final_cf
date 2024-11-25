import tkinter as tk
from tkinter import messagebox
from Algoritmos import binary_search
from Algoritmos import quicksort
from Algoritmos import recursion
from Algoritmos import selection_sort

class AlgorithmSelector:
    def __init__(self, root):
        self.root = root
        self.root.title("Selector de Algoritmos")

        # Etiqueta de instrucciones
        tk.Label(root, text="Selecciona un algoritmo para visualizar:").pack(pady=10)

        # Lista de opciones de algoritmos
        self.algorithms = {
            "Búsqueda Binaria": binary_search,
            "Quicksort": quicksort,
            "Recursión": recursion,
            "Ordenamiento por Selección": selection_sort
        }
        
        # Variable para almacenar la selección del usuario
        self.selected_algorithm = tk.StringVar(root)
        self.selected_algorithm.set("Búsqueda Binaria")  # Opción por defecto

        # Menú desplegable para seleccionar el algoritmo
        self.dropdown = tk.OptionMenu(root, self.selected_algorithm, *self.algorithms.keys())
        self.dropdown.pack(pady=10)

        # Botón para ejecutar el algoritmo seleccionado
        self.run_button = tk.Button(root, text="Ejecutar Algoritmo", command=self.run_algorithm)
        self.run_button.pack(pady=10)

    def run_algorithm(self):
        # Obtener el algoritmo seleccionado
        algorithm_name = self.selected_algorithm.get()
        algorithm_module = self.algorithms.get(algorithm_name)

        # Confirmación de ejecución
        if messagebox.askyesno("Confirmación", f"¿Quieres ejecutar el algoritmo '{algorithm_name}'?"):
            try:
                # Ejecutar el archivo del algoritmo seleccionado
                algorithm_module.main()  # Llama a la función principal en cada archivo de algoritmo
            except AttributeError:
                messagebox.showerror("Error", f"No se pudo encontrar la función 'main' en {algorithm_name}")
            except Exception as e:
                messagebox.showerror("Error", f"Ha ocurrido un error al ejecutar {algorithm_name}:\n{e}")

# Crear la ventana principal
root = tk.Tk()
app = AlgorithmSelector(root)
root.mainloop()
