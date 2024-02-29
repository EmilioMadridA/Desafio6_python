# Funciones externas
import preguntas as p

#Funcion
def verificar(alternativas, eleccion):
    """Funcion que permite comprobar si la respuesta entregada por el usuario es correcta.

    Args:
        alternativas (list): Lista de alternativas, correspondientes a una pregunta.
        eleccion (str): String (char) que ingresa el usuario, apuntando a una de las alternativas.

    Returns:
        bool: Se retorna True o False en caso de estar correcta o incorrecta la respuesta.
    """
    # Devuelve el índice de elección dada
    eleccion = ['a', 'b', 'c','d'].index(eleccion)

    # Verifica si la alternativa elegida es correcta
    if alternativas[eleccion][1] == 1:
        print('Respuesta Correcta')
        correcto = True
    else:
        print('Respuesta Incorrecta')
        correcto = False    
    return correcto



if __name__ == '__main__':
    from print_preguntas import print_pregunta
    
    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = p.pool_preguntas['básicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta['alternativas'], respuesta)






