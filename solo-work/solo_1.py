# zadanie 1.1

hello = "Hello"
student = "Ola"

# oczekiwany rezultat: Hello Ola
# wykorzystaj w princie zmienne hello i student
print("{} {}".format(hello, student))

# zadanie 1.2

student = input("Wpisz swoje imie: ")

print(f"Hello {student}")

# zadanie 1.3

studenci = ["Ania", "Kuba", "Piotr", "Jan"]

# policz liczbe studentow w tablicy studenci 
# oczekiwany rezultat: Liczba studentow wynosi: 4
liczba_studentow = len(studenci)
print(f"Liczba studentow wynosi: {liczba_studentow}")

# zadanie 1.4

studenci = ["Ania", "Kasia", "Piotr", "Tomek"]

# za pomoca petli i print przywitaj sie z kazdym studentem
# z tabeli studenci osobno
# oczekiwany rezultat:
# Hello Ania
# Hello Kasia
# Hello Piotr
# Hello Tomek
for student in studenci:
    print(f"Hello {student}")


# zadanie 1.5

liczba = 3
potega = 4

wynik = liczba**potega

# oczekiwany rezultat:
# Wynik wynosi: 81
print(f"Wynik wynosi: {wynik}")

# zadanie 1.6

# policz ilosc nawiasow ( w danym ciagu znakow

ciag_znakow = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"
liczba_nawiasow_otwierajacych = ciag_znakow.count('(')

# oczekiwany rezultat:
# Liczba nawiasow otwierajacych wynosi: 4
print("Liczba nawiasow otwierajacych wynosi: " + str(liczba_nawiasow_otwierajacych))

# zadanie 1.7

# posortuj alfabetycznie (od imienia) studentow
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
studenci.sort()
# oczekiwany rezultat:
# Anna Szczesny
# Barbara Kowalska
# Jan Niezbedny
# Tomasz Nijaki
print("Alfabetyczna lista studentow wynosi: ")
for student in studenci:
    print(student)

# zadanie 1.8

# posortuj alfabetycznie (od nazwiska) studentow
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]

def nazwiska(imie):
    return imie.split(" ")[-1]

studenci.sort(key=nazwiska)
# oczekiwany rezultat:
# Barbara Kowalska
# Jan Niezbedny
# Tomasz Nijaki
# Anna Szczesny
print("Alfabetyczna lista studentow wynosi: ")
for student in studenci:
    print(student)

# zadanie 1.9

# policz wszystkich studentow z tablicy, ktorych nazwisko zaczyna sie na N
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
N = 0
for student in studenci:
    if student.split(" ")[-1].startswith("N"):
        N += 1
print(f"Liczba studentow na N wynosi: {N}")

# zadanie 1.10

# zmienne ponizej reprezentuja ulozenie punktow na wykresie,
# do zadania dolaczono takze rysunek pomocniczy
wykres_1 = [[2, 4], [4, 4], [6, 4]]
wykres_2 = [[2, 3], [4, 4], [6, 5]]
wykres_3 = [[2, 3], [4, 3], [5, 4]]

# zbadaj kazdy wykres, czy dla wyznaczonych punktow istnieje funkcja
# liniowa laczaca punkty
# jesli sie nie da, to zwroc False
# jesli sie da, zwroc True

def is_linear(w):
    left = (w[1][1] - w[0][1]) / (w[1][0] - w[0][0])
    right = (w[2][1] - w[0][1]) / (w[2][0] - w[0][0])
    return(left==right)
    
wykresy = [wykres_1, wykres_2, wykres_3]
wyniki = []

for wykres in wykresy:
    wyniki.append(is_linear(wykres))

for id, w in enumerate(wyniki):
    if w is True:
        print(f"Dla punktów na wykresie {id+1} można wyznaczyć funkcję liniową")
    else:
        print(f"Dla punktów na wykresie {id+1} nie można wyznaczyć funkcji liniowej")

