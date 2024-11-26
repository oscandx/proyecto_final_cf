# Proyecto de Visualización de Algoritmos con Tkinter y FastAPI

## Descripción

Este proyecto es una herramienta educativa interactiva que permite a los usuarios visualizar el funcionamiento paso a paso de varios algoritmos fundamentales. Utiliza **Tkinter** para la interfaz gráfica y **FastAPI** para manejar solicitudes desde una API en Swagger, permitiendo ingresar arreglos y obtener resultados de los algoritmos implementados.

## Características principales

- **Algoritmos disponibles:**
  - Búsqueda binaria
  - Ordenamiento por selección
  - Quicksort
  - Recursión
- **Visualización paso a paso:** Los usuarios pueden ver cada paso del algoritmo en la interfaz gráfica.
- **FastAPI integrado:** Permite ingresar arreglos desde Swagger y ver los resultados procesados por los algoritmos.
- **Swagger UI:** Acceso a una interfaz interactiva para probar la API.

## Requisitos

- **Python 3.8 o superior**
- **Tkinter**
- **FastAPI**
- **Uvicorn** (para correr el servidor FastAPI)

## Instalación

1. **Clona este repositorio:**
   git clone https://github.com/oscandx/proyecto_final_cf.git

2. **Instala dependencias:**
    pip install -r requirements.txt

3. **Ejecuta la interfaz gráfica:**
    python main_tkinter.py

4. **Levanta el servidor FastAPI:**
    uvicorn main_fastapi:app --reload
    Abre Swagger en tu navegador: http://localhost:8000/docs

## Uso

### Interfaz gráfica (Tkinter)
- Abre la aplicación Tkinter.
- Ingresa los elementos en la lista y selecciona el algoritmo.
- Observa el paso a paso del proceso.

### FastAPI y Swagger
- Accede a **Swagger** en http://localhost:8000/docs.
- Prueba los endpoints disponibles para cada algoritmo, ingresando un arreglo.
- Los resultados se devolverán en formato **JSON**.