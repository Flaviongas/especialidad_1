from tests import common_cases, edge_cases, error_cases
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
    # TODO: Usar unittest
    common_cases(calcular_area_rectangulo, calcular_area_triangulo)
    edge_cases(calcular_area_rectangulo, calcular_area_triangulo)
    error_cases(calcular_area_rectangulo, calcular_area_triangulo)
