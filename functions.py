import math
from typing import List
import math

def bhaskara(a, b, c, delta):
    list= []

    deltaSqrt = math.sqrt(delta)

    x1 = (-b + deltaSqrt) / (2 * a)
    x2 = (-b - deltaSqrt) / (2 * a)

    list.append(x1)
    list.append(x2)

    return list
