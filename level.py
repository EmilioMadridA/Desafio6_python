# Funcion
def choose_level(n_pregunta, p_level):
    """Funcion que permite escoger el nivel de dificultad de la pregunta a realizar.

    Args:
        n_pregunta (int): Variable que indica el "número de la pregunta".
        p_level (int): Variable que indica las preguntas por nivel, lo que determina cuantas preguntas se realizarán.

    Returns:
        str: Retorna el nivel de la pregunta que se está evaluando.
    """
    # Definir rangos de preguntas por nivel basados en p_level
    rangos = {
        1 : [('básicas', [1]), ('intermedias', [2]), ('avanzadas', [3])],
        2 : [('básicas', [1, 2]), ('intermedias', [3, 4]), ('avanzadas', [5, 6])],
        3 : [('básicas', [1, 2, 3]), ('intermedias', [4, 5, 6]), ('avanzadas', [7, 8, 9])]
    }
    
    # Ciclo for para encontrar el nivel basado en n_pregunta y p_level
    for nivel, rango in rangos.get(int(p_level), []):
        if n_pregunta in rango:
            level = nivel
            return level
        else:
            level = "Nivel no definido"
    return level


if __name__ == '__main__':
    # verificar resultados
    print(choose_level(6, 2)) # básicas
    print(choose_level(4, 2)) # intermedias
    print(choose_level(7, 3)) # avanzadas
    print(choose_level(8, 3)) # intermedias