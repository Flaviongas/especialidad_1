
def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.
    :param base: La base del rectángulo. :param altura: La altura del rectángulo.
    :return: El área del rectángulo.
    """
    if base < 0 or altura < 0:
        raise ValueError("La base y la altura deben ser números positivos.")
    return base*altura


def calcular_area_triangulo(base, altura):
    """
    Calcula el área de un triángulo.
    :param base: La base del triángulo.
    :param altura: La altura del triángulo. :return: El área del triángulo.
    """
    if base < 0 or altura < 0:
        raise ValueError("La base y la altura deben ser números positivos.")
    return (base * altura) / 2


# Ejemplo de uso
if __name__  == "__main__":
    try:
        print("Área del rectángulo:", calcular_area_rectangulo(5, 10))
        print("Área del triángulo:", calcular_area_triangulo(5, 10)) 
    except ValueError as e:
        print(e)
