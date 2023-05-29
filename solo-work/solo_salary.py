import pandas as pd

class Pracownik:
    def __init__(self, imie, nazwisko, wynagrodzenie_brutto):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wynagrodzenie_brutto = wynagrodzenie_brutto

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'
    
    def oblicz_netto(self):
        skl_em = round(self.wynagrodzenie_brutto * 0.0976, 2)
        skl_ren = round(self.wynagrodzenie_brutto * 0.015, 2)
        skl_chor = round(self.wynagrodzenie_brutto * 0.0245, 2)
        skl_zdr = round((self.wynagrodzenie_brutto - (skl_em + skl_ren + skl_chor)) * 0.09, 2)
        pit = round(((self.wynagrodzenie_brutto * 12 * 0.12) - 3600)/12)
        wynagrodzenie_netto = self.wynagrodzenie_brutto - (skl_em + skl_ren + skl_chor + skl_zdr + pit)
        return wynagrodzenie_netto    
    
    def oblicz_koszty(self):
        skl_em = round(self.wynagrodzenie_brutto * 0.0976 ,2)
        skl_ren = round(self.wynagrodzenie_brutto * 0.065, 2)
        skl_wyp = round(self.wynagrodzenie_brutto * 0.0167, 2)
        skl_FP = round(self.wynagrodzenie_brutto * 0.0245, 2)
        skl_FGSP = round(self.wynagrodzenie_brutto * 0.001, 2)
        koszty = round(self.wynagrodzenie_brutto + skl_em + skl_ren + skl_wyp + skl_FP + skl_FGSP, 2)
        return koszty

#reading csv
pracownicy_df = pd.read_csv(r'salary.csv')
pracownicy = []

#creating class instances and appending them to the list
for index, p in pracownicy_df.iterrows():
    pracownicy.append(Pracownik(p[0],p[1],p[2]))

koszty_wszystkich_pracownikow = 0

#checking self
print(str(pracownicy[0]))

#printing emp info
for p in pracownicy:
    print(f"Pracownik {p.imie} {p.nazwisko}: ")
    print(f"- pensja brutto: {round(p.wynagrodzenie_brutto,2)}")
    print(f"- pensja netto: {p.oblicz_netto()}")
    print(f"- koszt pracodawcy: {p.oblicz_koszty()}")
    koszty_wszystkich_pracownikow += p.oblicz_koszty()

print(f"Suma kosztów wynosi: {koszty_wszystkich_pracownikow}")