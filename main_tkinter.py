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

        # Se genera una etiqueta de instrucciones
        tk.Label(root, 
                 text="""Este programa genera una visualización interactiva de algunos algoritmos más usados en programación.
                        Selecciona un algoritmo para visualizar:""", 
                 font=("Comic sans ms", 14)).pack(pady=10)

        # Se genera un marco para los botones de selección
        self.options_frame = tk.Frame(root)
        self.options_frame.pack(pady=10)

        # Se crea un diccionario con los algoritmos
        self.algorithms = {
            "Búsqueda Binaria": binary_search,
            "Quicksort": quicksort,
            "Recursión": recursion,
            "Ordenamiento por Selección": selection_sort
        }
        
        # Se crea una variable para almacenar la selección del usuario
        self.selected_algorithm = tk.StringVar(root)
        self.selected_algorithm.set("Búsqueda Binaria")  # Por defecto

        # Creación de botones de selección
        for name in self.algorithms.keys():
            tk.Radiobutton(
                self.options_frame,
                text=name,
                variable=self.selected_algorithm,
                value=name,
                font=("Comic sans ms", 12)
            ).pack(anchor="w")

        # Botón para ejecutar el algoritmo seleccionado
        self.run_button = tk.Button(root, text="Ejecutar Algoritmo", font=("Comic sans ms", 12), command=self.run_algorithm)
        self.run_button.pack(pady=20)

    def run_algorithm(self):
        # Se obtiene el algoritmo seleccionado
        algorithm_name = self.selected_algorithm.get()
        algorithm_module = self.algorithms.get(algorithm_name)

        # Confirmación de ejecución
        if messagebox.askyesno("Confirmación", f"¿Quieres ejecutar el algoritmo '{algorithm_name}'?"):
            try:
                # Se ejecuta la función principal del algoritmo seleccionado
                algorithm_module.main()  # Supone que cada módulo tiene una función `main()`
            except AttributeError:
                messagebox.showerror("Error", f"No se pudo encontrar la función 'main' en {algorithm_name}")
            except Exception as e:
                messagebox.showerror("Error", f"Ha ocurrido un error al ejecutar {algorithm_name}:\n{e}")

# Creación de la ventana principal
root = tk.Tk()
app = AlgorithmSelector(root)
root.mainloop()
