import math
from typing import List
import math

#função para calcular os valores de x' e x" com a formula de bhaskara
def bhaskara(a, b, c, delta):
    list= []

    #convertendo String para float
    a = float(a)
    b = float(b)
    c = float(c)
    delta = float(delta)

    deltaSqrt = math.sqrt(delta)

    x1 = (-b + deltaSqrt) / (2 * a)
    x2 = (-b - deltaSqrt) / (2 * a)

    list.append(x1)
    list.append(x2)

    return list
