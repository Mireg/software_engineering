class Trojkat:
    def __init__(self, a, b, c, h_a):
        self.a = a
        self.b = b
        self.c = c
        self.h_a = h_a
        # self.obwod = a + b + c
    
    def obwod(self):
        return(self.a + self.b + self.c)
    
    
    def pole(self):
        return((self.a * self.h_a) / 2)

class Kwadrat:
    def __init__(self, a):
        self.a = a

    
    def obwod(self):
        return(4 * self.a)
    
    def pole(self):
        return(pow(self.a))

print('-----------------------------------------------')

class Student:
    def __init__(self, imie, nazwisko, numer_indeksu):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_indeksu = numer_indeksu
        self.oceny = []
    
    
    def __str__(self):
        return(f"{self.imie} {self.nazwisko} {self.numer_indeksu}")
    

    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena)


    def zwroc_srednia(self):
        return(sum(self.oceny) / len(self.oceny))

# trojkat_rownoboczny = Trojkat(10, 10, 10, 8)
# moj_trojkat = Trojkat(6, 6, 6, 5)
# print(trojkat_rownoboczny.obwod())
# print(moj_trojkat.obwod())
# print(f'Mój trójkąt obwód: {moj_trojkat.obwod()}')
# print(f'Mój trójkąt pole: {moj_trojkat.pole()}')


# moj_kwadrat = Kwadrat(17)
# print(f'Mój kwadrat obwód: {moj_kwadrat.obwod()}')
# print(f'Mój kwadrat pole: {moj_kwadrat.pole()}')

student_mariusz = Student("Mariusz", "Kowalski", 123456)
print(student_mariusz)

student_mariusz.dodaj_ocene(4.5)
student_mariusz.dodaj_ocene(3)

print(student_mariusz.zwroc_srednia())