import math


def trojkat(bok_a, bok_b, bok_c, wysokosc_a):
    obwod = bok_a + bok_b + bok_c
    pole = (bok_a * wysokosc_a) / 2
    return obwod, pole

print(trojkat(3, 4, 5, 2.5))

# kwadrat, prostokat dla studenta 1
def kwadrat(bok):
    obwod = 4 * bok
    pole = pow(bok, 2) 
    return obwod, pole

def prostokat(bok_a, bok_b):
    obwod = 2 * bok_a + 2* bok_b
    pole = bok_a * bok_b
    return obwod, pole

# rownoleglobok i romb dla studenta 2
def rownoleglobok(bok_a, bok_b, wysokosc_a):
    obwod = bok_a*2 +bok_b*2
    pole = bok_a*wysokosc_a
    return obwod, pole


def romb(bok, wysokosc):
    obwod = bok*4
    pole = bok*wysokosc
    return obwod, pole

# trapez i kolo dla studenta 3
def trapez(bok_a, bok_b, bok_c, bok_d, wysokosc_a):
    obwod = (bok_a + bok_b + bok_c + bok_d)
    pole = ((bok_a + bok_b)*wysokosc_a)/2
    return obwod, pole


def kolo(promien):
<<<<<<< HEAD
    obwod = 2 * math.pi * promien
    pole = math.pi * promien ** 2
    return 0, 0
 
assert trojkat(10, 15, 16, 8) == (41, 40)
assert trojkat(3, 4, 5, 2.5) == (12, 3.75)
assert kwadrat(20) == (80, 400)
assert kwadrat(420) == (1680, 176400)
assert prostokat(12, 10) == (44, 120)
assert prostokat(3, 2) == (10, 6)
assert rownoleglobok(6, 5, 2) == (22, 12)
assert romb(10, 5) == (40, 50)
assert trapez(10, 15, 7, 14, 2) == (45, 25)
=======
    obwod = round(2 * math.pi * promien, 2)
    pole = round(math.pi * promien ** 2, 2)
    return obwod, pole


# assert trojkat(10, 15, 16, 8) == (41, 40)
# assert kwadrat(20) == (80, 400)
# assert prostokat(12, 10) == (44, 120)
# assert rownoleglobok(6, 5, 2) == (22, 12)
# assert romb(10, 5) == (40, 50)

assert trapez(10, 15, 7, 14, 7) == (46, 87.5)
assert trapez(10,14,8,8,9) == (40, 108) 
assert kolo(5) == (31.42, 78.54)
>>>>>>> 575ddc0ae1294e11fe138c30fe4793194e35589c
