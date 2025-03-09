# Identificación de casos de prueba
def common_cases(calcular_area_rectangulo, calcular_area_triangulo):
    try:

        print("Casos comunes:")

        # Enteros
        assert calcular_area_rectangulo(5, 10) == 50
        assert calcular_area_triangulo(5, 10) == 25
        print("Enteros: OK")
        # Floats
        assert calcular_area_rectangulo(5.5, 10.5) == 57.75
        assert calcular_area_triangulo(5.5, 10.5) == 28.875
        print("Floats: OK")

    except ValueError as e:
        print(e)

def edge_cases(calcular_area_rectangulo, calcular_area_triangulo):
    try:

        print("Casos límite:")

        # Enteros
        assert calcular_area_rectangulo(0, 0) == 0
        assert calcular_area_triangulo(0, 0) == 0
        print("Enteros: OK")
        # Floats
        assert calcular_area_rectangulo(0.0, 0.0) == 0.0
        assert calcular_area_triangulo(0.0, 0.0) == 0.0
        print("Floats: OK")
        # Negativos
        calcular_area_rectangulo(-5, 10)
        calcular_area_triangulo(-5, 10)

    except ValueError as e:
        if str(e) == "La base y la altura deben ser números positivos.":
            print("Negativos: OK")

def error_cases(calcular_area_rectangulo, calcular_area_triangulo):
    try:

        print("Casos de error:")

        # Strings
        calcular_area_rectangulo("5", 10)
        calcular_area_triangulo("5", 10)
        calcular_area_rectangulo(5, "10")
        calcular_area_triangulo(5, "10")
        print("Strings: OK")

        # None
        calcular_area_rectangulo(None, 10)
        calcular_area_triangulo(None, 10)
        calcular_area_rectangulo(5, None)
        calcular_area_triangulo(5, None)
        print("None: OK")

        # NaN
        calcular_area_rectangulo(float("nan"), 10)
        calcular_area_triangulo(float("nan"), 10)
        calcular_area_rectangulo(5, float("nan"))
        calcular_area_triangulo(5, float("nan"))
        print("NaN: OK")
    except TypeError as e:
        if str(e) == "La base y la altura deben ser números positivos.":
            print("Strings: OK")

