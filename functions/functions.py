# Ejemplos de funciones incorporadas
type(42)
print(type(42))

# Para convertir enteros
print(int(3.5))

# Este es un módulo de operaciones matemáticas en Python
from fractions import Fraction
import math
print(math.ceil(3.5))

print(math.ceil(3.5))

print(math.sqrt(81))

print(math.pi)

# Calcular el volumen de una esfera - Fórmula 4/3 pi r3

from math import pi
r = float(input(5))
volumen = 4/3 * pi * r ** 3

print("El volumen de la esfera es {} unidades cúbicas".format(volumen))
