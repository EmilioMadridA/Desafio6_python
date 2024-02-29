# Librerias y/o funciones externas
import preguntas as p
import random
from shuffle import shuffle_alt

# Funcion
def choose_q(dificultad):
    """ Funcion que toma como único argumento la dificultad de la pregunta, a partir de eso, tomas las preguntas correspondientes a la dificultad ingresada.

    Args:
        dificultad (str): Dificultad que apunta a un set de preguntas

    Returns:
        pregunta (str): Enunciado correspondiente a la pregunta del set de preguntas correspondiente a la dificultad.
        alternativas (list): Elemento de la lista que pertenece a las alternativas de la pregunta correspondiete.
    """
    # Opciones dadas para escoger.
    opciones = {
        'básicas': [1,2,3],
        'intermedias': [1,2,3],
        'avanzadas': [1,2,3]
        }
    # Escoger una pregunta
    n_elegido = random.choice(opciones[dificultad])

    # Eliminarla del ambiente global para no escogerla de nuevo
    opciones[dificultad].remove(n_elegido)
    
    # Escoger enunciado y alternativas mezcladas
    pregunta = p.pool_preguntas[dificultad][f'pregunta_{n_elegido}']['enunciado']
    alternativas = shuffle_alt(p.pool_preguntas[dificultad][f'pregunta_{n_elegido}'])
    
    return pregunta, alternativas

if __name__ == '__main__':
    # si ejecuto el programa, las preguntas cambian de orden, pero nunca debieran repetirse
    pregunta, alternativas = choose_q('básicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('intermedias')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('avanzadas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')