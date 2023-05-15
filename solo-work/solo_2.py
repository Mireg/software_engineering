class Trojkat:
    def __init__(self, a, b, c, h_a):
        self.a = a
        self.b = b
        self.c = c
        self.h_a = h_a
        # self.obwod = a + b + c
    
    def obwod(self):
        return(self.a + self.b + self.c)


trojkat_rownoboczny = Trojkat(10, 10, 10, 8)

print(trojkat_rownoboczny.obwod())
