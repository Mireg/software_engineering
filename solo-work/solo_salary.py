import pandas as pd

class Pracownik:
    def __init__(self, imie, nazwisko, wynagrodzenie_brutto):
        self.imie = imie
        self.nazwisko= nazwisko
        self.wynagrodzenie_brutto = wynagrodzenie_brutto

    def __str_(self):
        return self.imie + self.nazwisko 
    
    def oblicz_netto(self):
        skl_em = self.wynagrodzenie_brutto * 0.0976
        skl_ren = self.wynagrodzenie_brutto * 0.015
        skl_chor = self.wynagrodzenie_brutto * 0.0245
        skl_zdr = (self.wynagrodzenie_brutto * self.wynagrodzenie_brutto - (skl_em + skl_ren + skl_chor)) * 0.09 - 279.58
        wynagrodzenie_netto = skl_em + skl_ren + skl_chor + skl_zdr
        return wynagrodzenie_netto    
    
    def oblicz_koszty(self):
        return 0

pracownicy_pd = pd.read_csv(r'salary.csv')

koszty_wszystkich_pracownikow = 0

# for pracownik in pracownicy:
#      print(f"Pracownik {pracownik['imie']}: ")
#     print("- pensja brutto: ")
#     print("- pensja netto: ")
#     print("- koszt pracodawcy: ")
#     print("- koszt całkowity: ")

for index, pracownik in pracownicy.iterrows():
    print(f"Pracownik {pracownik['imie']} {pracownik['nazwisko']}:")
    print(f"- pensja brutto: {pracownik['wynagrodzenie_brutto']}")
#    print(f"- pensja netto: {}")
#     print("- koszt pracodawcy: ")
#     print("- koszt całkowity: ")

print("Suma kosztów wynosi: xxx")