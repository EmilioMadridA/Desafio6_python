# Funcion externa
import preguntas as p

# Funcion
def print_pregunta(enunciado, alternativas):
    """Funcion que permite mostrar en la app las preguntas de acuerdo a un formato.

    Args:
        enunciado (list): Lista de un único elemento, correpondiente a la clave 'enunciado' de la pregunta correspondiente.
        alternativas (list): Lista que incluye las alternativas de la pregunta correspondiente.
    """
    # Impresión enunciado
    print(enunciado[0])
    # Salto de lina  
    print()
    
    # Letras para asociar con las alternativas
    letras = ['A', 'B', 'C', 'D']
    
    # Imprimir cada alternativa con su letra correspondiente
    for i, alternativa in enumerate(alternativas):
        print(f"{letras[i]}. {alternativa[0]}")
        
if __name__ == '__main__':
    # Las preguntas y alternativas deben mostrarse según lo indicado
    pregunta = p.pool_preguntas['intermedias']['pregunta_3']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    
    # Enunciado básico 1

    # A. alt_1
    # B. alt_2
    # C. alt_3
    # D. alt_4