import unittest
import tkinter as tk
from unittest.mock import patch, MagicMock
from main_tkinter import AlgorithmSelector  
from Algoritmos import binary_search, quicksort, recursion, selection_sort

class TestAlgorithmSelector(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()  
        self.app = AlgorithmSelector(self.root)

    def test_initial_selection(self):
        self.assertEqual(self.app.selected_algorithm.get(), "Búsqueda Binaria")

    def test_algorithm_selection_change(self):
        self.app.selected_algorithm.set("Quicksort")
        self.assertEqual(self.app.selected_algorithm.get(), "Quicksort")

    @patch('tkinter.messagebox.askyesno', return_value=True)  # Parchea messagebox
    @patch('Algoritmos.binary_search.main')  # Parchea la función main del módulo binary_search
    def test_run_algorithm_binary_search(self, mock_main, mock_askyesno):
        self.app.selected_algorithm.set("Búsqueda Binaria")
        self.app.run_algorithm()  # Llama a la función del botón
        mock_main.assert_called_once()  # Verifica que se llamó a main()

    @patch('tkinter.messagebox.askyesno', return_value=True)
    @patch('Algoritmos.quicksort.main')
    def test_run_algorithm_quicksort(self, mock_main, mock_askyesno):
        self.app.selected_algorithm.set("Quicksort")
        self.app.run_algorithm()
        mock_main.assert_called_once()

    def tearDown(self):
        self.root.destroy()

if __name__ == '__main__':
    unittest.main()