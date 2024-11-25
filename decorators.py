import time

def timing_decorator(func):
    """
    Un decorador que mide el tiempo de ejecución de una función.

    Este decorador envuelve una función y mide el tiempo que tarda en ejecutarse. 
    El tiempo de ejecución se imprime en la consola con el nombre de la función y el tiempo en segundos.

    Args:
        func (function): La función que se desea envolver y medir el tiempo de ejecución.

    Returns:
        function: La función decorada que, al ejecutarse, imprimirá el tiempo que tardó en completarse.
    
    Ejemplo de uso:
        @timing_decorator
        def mi_funcion():
            # código de la función
            pass
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Tiempo de ejecución de {func.__name__}: {end_time - start_time:.4f} segundos")
        return result
    return wrapper