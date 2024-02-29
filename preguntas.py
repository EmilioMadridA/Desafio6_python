# Funcion
def crear_preguntas(dificultad):
    """Funcion para la generación de los diccionarios de las preguntas, enunciados y alternativas correspondientes a cada nivel. 

    Args:
        dificultad (str): Determina el nivel de las preguntas, enunciados y alternativas

    Returns:
        diccionario: Diccionario contruido, que consta de 3 preguntas, cada una con un enunciado, y una lista de alternativas.
    """
    # Se inicializa la variable a trabajar
    preguntas = {}
    # Se determinan los valores correspondientes a los enunciados de cada nivel.
    dificultades = {'básicas': 'básico', 'intermedias': 'intermedio', 'avanzadas': 'avanzado'}
    # Variable que obtiene el valor del enunciado correspondiente al nivel.
    enunciado_dificultad = dificultades.get(dificultad, dificultad)
    
    # Ciclo for, que permite la creación del diccionario correspondiente
    for i in range(1, 4):
        preguntas[f'pregunta_{i}'] = {
            'enunciado': [f'Enunciado {enunciado_dificultad} {i}'],
            'alternativas': [
                ['alt_1', 0],
                ['alt_2', 1],
                ['alt_3', 0],
                ['alt_4', 0]
            ]
        }
    # Retorno del diccionario procesado
    return preguntas

preguntas_basicas = crear_preguntas('básicas')
preguntas_intermedias = crear_preguntas('intermedias')
preguntas_avanzadas = crear_preguntas('avanzadas')

pool_preguntas = {'básicas': preguntas_basicas,
                  'intermedias': preguntas_intermedias,
                  'avanzadas': preguntas_avanzadas}