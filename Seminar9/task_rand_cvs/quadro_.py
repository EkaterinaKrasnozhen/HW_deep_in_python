
def quadric_eq(a, b, c):
    """нахождение корней квадратного уравнения
    """
    d = b**2 - 4 * a * c
    x1 = (-1) * b + d**0.5 / 2 * a
    x2 = (-1) * b - d**0.5 / 2 * a
    
    print(d, x1, x2)