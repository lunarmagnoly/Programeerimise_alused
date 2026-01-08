

"""
Loo programm, mis küsib kasutajalt ruutvõrrandi liikmete (
ruutliige, lineaarliige, vabaliige) kordajad ning arvutab nende põhjal diskriminandi ja
väljastab selle põhjal ruutvõrrandi lahendid.
Nagu tead, võib lahendeid vastavalt diskriminandi väärtusele olla üks või kaks, kuid lahendid võivad ka puududa.
"""
from math import sqrt


def solve_quadratic_equation(a: float, b: float, c: float):
    d = b**2 -(4 * a * c)
    if d == 0:
        return f"Ruutvõrrandi lahendus on {- b / (2 * a)}"
    elif d > 0:
        x1 = (- b + sqrt(d)) /(2 * a)
        x2 = (- b - sqrt(d)) /(2 * a)
        return f"Ruutvõrrandi lahendid on {x1} ja {x2}"
    else:
        return "Ruutvõrrandil ei ole lahendust"


if __name__ == '__main__':
    print("Ruutvõrrandi lahendamis programm: ")
    a = float(input("Sisestage a "))
    b = float(input("Sisestage b "))
    c = float(input("Sisestage c "))
    print(solve_quadratic_equation(a ,b ,c))
