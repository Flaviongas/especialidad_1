import pytest
from area import calcular_area_rectangulo as area_rectangulo, calcular_area_triangulo as area_triangulo
from numpy import isnan

def test_common_cases():
    print("Casos comunes: \n")

    # Enteros
    assert area_rectangulo(5, 10) == 50
    assert area_triangulo(5, 10) == 25
    print("Enteros: OK \n")

    # Floats
    assert area_rectangulo(5.5, 10.5) == 57.75
    assert area_triangulo(5.5, 10.5) == 28.875
    print("Floats: OK \n")

def test_edge_cases():
    print("Casos límite: \n")

    # Enteros
    assert area_rectangulo(0, 0) == 0
    assert area_triangulo(0, 0) == 0
    print("Enteros: OK \n")

    # Floats
    assert area_rectangulo(0.0, 0.0) == 0.0
    assert area_triangulo(0.0, 0.0) == 0.0
    print("Floats: OK \n")

    # Negativos
    with pytest.raises(ValueError):
        area_rectangulo(-5, 10)
    with pytest.raises(ValueError):
        area_triangulo(-5, 10)
    print("Negativos: OK \n")

def test_error_cases():
    print("Casos de error: \n")

    # Strings
    with pytest.raises(TypeError):
        area_rectangulo("5", 10)
    with pytest.raises(TypeError):
        area_triangulo("5", 10)
    with pytest.raises(TypeError):
        area_rectangulo(5, "10")
    with pytest.raises(TypeError):
        area_triangulo(5, "10")
    print("Strings: OK \n")

    # None
    with pytest.raises(TypeError):
        area_rectangulo(None, 10)
    with pytest.raises(TypeError):
        area_triangulo(None, 10)
    with pytest.raises(TypeError):
        area_rectangulo(5, None)
    with pytest.raises(TypeError):
        area_triangulo(5, None)
    print("None: OK \n")

    # NaN
    nan = float("nan")
    assert isnan(area_rectangulo(nan, 10))
    assert isnan(area_rectangulo(10, nan))
    assert isnan(area_triangulo(nan, 10))
    assert isnan(area_triangulo(10, nan))
    print("NaN: OK \n")
