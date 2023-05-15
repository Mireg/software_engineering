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
    

trojkat_rownoboczny = Trojkat(10, 10, 10, 8)
moj_trojkat = Trojkat(6, 6, 6, 5)
print(trojkat_rownoboczny.obwod())
print(moj_trojkat.obwod())
print(f'Mój trójkąt obwód: {moj_trojkat.obwod()}')
print(f'Mój trójkąt pole: {moj_trojkat.pole()}')


moj_kwadrat = Kwadrat(17)
print(f'Mój kwadrat obwód: {moj_kwadrat.obwod()}')
print(f'Mój kwadrat pole: {moj_kwadrat.pole()}')