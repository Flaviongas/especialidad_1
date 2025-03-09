import unittest
from area import calcular_area_rectangulo as area_rectangulo, calcular_area_triangulo as area_triangulo
from numpy import isnan

class Tests(unittest.TestCase):

    def test_common_cases(self):
        try:
            print("Casos comunes: \n")

            # Enteros
            self.assertEqual(area_rectangulo(5, 10), 50)
            self.assertEqual(area_triangulo(5, 10), 25)
            print("Enteros: OK \n")
            # Floats
            self.assertEqual(area_rectangulo(5.5, 10.5), 57.75)
            self.assertEqual(area_triangulo(5.5, 10.5), 28.875)
            print("Floats: OK \n")

        except ValueError as e:
            print(e)

    def test_edge_cases(self):
        try:
            print("Casos límite: \n")

            # Enteros
            self.assertEqual(area_rectangulo(0, 0), 0)
            self.assertEqual(area_triangulo(0, 0), 0)
            print("Enteros: OK \n")
            # Floats
            self.assertEqual(area_rectangulo(0.0, 0.0), 0.0)
            self.assertEqual(area_triangulo(0.0, 0.0), 0.0)
            print("Floats: OK \n")
            # Negativos
            with self.assertRaises(ValueError):
                area_rectangulo(-5, 10)
            with self.assertRaises(ValueError):
                area_triangulo(-5, 10)
            print("Negativos: OK \n")

        except Exception as e:
            print(e)

    def test_error_cases(self):
        try:
            print("Casos de error: \n")

            # Strings
            with self.assertRaises(TypeError):
                area_rectangulo("5", 10)
            with self.assertRaises(TypeError):
                area_triangulo("5", 10)
            with self.assertRaises(TypeError):
                area_rectangulo(5, "10")
            with self.assertRaises(TypeError):
                area_triangulo(5, "10")
            print("Strings: OK \n")

            # None
            with self.assertRaises(TypeError):
                area_rectangulo(None, 10)
            with self.assertRaises(TypeError):
                area_triangulo(None, 10)
            with self.assertRaises(TypeError):
                area_rectangulo(5, None)
            with self.assertRaises(TypeError):
                area_triangulo(5, None)
            print("None: OK \n")

            # NaN
            nan = float("nan")
            self.assertTrue(isnan(area_rectangulo(nan, 10)))
            self.assertTrue(isnan(area_rectangulo(10, nan)))
            self.assertTrue(isnan(area_triangulo(nan, 10)))
            self.assertTrue(isnan(area_triangulo(10, nan)))
            print("NaN: OK \n")
        except TypeError as e:
            if str(e) == "La base y la altura deben ser números positivos.":
                print("Strings: OK")

if __name__  == "__main__":
    unittest.main()
