from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from Algoritmos.binary_search import binary_search_f
from Algoritmos.selection_sort import selection_sort_f
from Algoritmos.quicksort import quicksort_f

app = FastAPI()

# se crea el modelo para solicitudes de entrada
class ArrayRequest(BaseModel):
    arr: List[int]

class SearchRequest(ArrayRequest):
    target: int


# endpoint de búsqueda binaria
@app.post("/binary-search/")
async def binary_search_endpoint(request: SearchRequest):
    sorted_arr = quicksort_f(request.arr)  # Aseguramos que la lista esté ordenada
    result = binary_search_f(sorted_arr, request.target)
    if result is None:
        return {"message": "Número no encontrado en la lista."}
    return {"message": f"Número encontrado en la posición {result} (en lista ordenada)"}

# endpoint de ordenamiento con quicksort
@app.post("/quicksort/")
async def quicksort_endpoint(request: ArrayRequest):
    sorted_arr = quicksort_f(request.arr)
    return {"sorted_array": sorted_arr}

# endpoint de ordenamiento con selección
@app.post("/selection-sort/")
async def selection_sort_endpoint(request: ArrayRequest):
    sorted_arr = selection_sort_f(request.arr)
    return {"sorted_array": sorted_arr}




