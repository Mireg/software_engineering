import pandas as pd

class Pracownik:
    def __init__(self, imie, nazwisko, wynagrodzenie_brutto):
        self.imie = imie
        self.nazwisko= nazwisko
        self.wynagrodzenie_brutto = wynagrodzenie_brutto

    def __str_(self):
        return self.imie + self.nazwisko 
    
    def oblicz_netto(self):
        skl_em = round(self.wynagrodzenie_brutto * 0.0976, 2)
        skl_ren = round(self.wynagrodzenie_brutto * 0.015, 2)
        skl_chor = round(self.wynagrodzenie_brutto * 0.0245, 2)
        skl_zdr = round((self.wynagrodzenie_brutto - (skl_em + skl_ren + skl_chor)) * 0.09, 2)
        pit = round(((self.wynagrodzenie_brutto * 12 * 0.12) - 3600)/12)
        wynagrodzenie_netto = self.wynagrodzenie_brutto - (skl_em + skl_ren + skl_chor + skl_zdr + pit)
        return wynagrodzenie_netto    
    
    def oblicz_koszty(self):
        return 0

pracownicy_df = pd.read_csv(r'salary.csv')
pracownicy = []

for index, p in pracownicy_df.iterrows():
    pracownicy.append(Pracownik(p[0],p[1],p[2]))

koszty_wszystkich_pracownikow = 0

for p in pracownicy:
    print(f"Pracownik {p.imie} {p.nazwisko}: ")
    print(f"- pensja brutto: {p.wynagrodzenie_brutto}")
    print(f"- pensja netto: {p.oblicz_netto()}")
#    print(f"- koszt pracodawcy: ")
#    print(f"- koszt całkowity: ")

print("Suma kosztów wynosi: xxx")