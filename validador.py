# Funcion
def validate(opciones, eleccion):
    """Funcion que permite validar si un valor se encuentra incluido en un conjunto de opciones
    
    Args:
        opciones (list): Lista de opciones válidas a evaluar
        eleccion (str): Variable obtenida desde input, y es el valor a evaluar si se encuentra dentro de "opciones"

    Returns:
        str: Retorna el valor obtenido desde input, almacenado en "eleccion", en caso de ser válido
    """
    while eleccion not in opciones:
        print(f"Opción no válida, ingrese una de las opciones válidas: {', '.join(opciones)}")
        eleccion = input('Ingresa una Opción: ').lower()
    return eleccion


if __name__ == '__main__':
    
    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ['0','1']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(numeros, eleccion)
    
    
