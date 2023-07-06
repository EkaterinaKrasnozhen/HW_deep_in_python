
from Deco import start_quadro_fromcsv as dec_start, cache_to_json as cache


@dec_start
@cache
def quadric_eq(a, b, c):
    """нахождение корней квадратного уравнения
    """
    d = b**2 - 4 * a * c
    x1 = (-1) * b + d**0.5 / 2 * a
    x2 = (-1) * b - d**0.5 / 2 * a
    return (d, x1, x2)
    
    
if __name__ == '__main__':
    quadric_eq(1,2,3)