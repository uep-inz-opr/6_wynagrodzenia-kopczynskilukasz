liczba_pracownikow = int(input())
class Worker:
    def __init__(self,imie,wynagrodzenie_brutto):
        self.imie = imie
        self.wynagrodzenie_brutto = wynagrodzenie_brutto
        self.skladka = round(self.wynagrodzenie_brutto*0.0976,2) + round(self.wynagrodzenie_brutto*0.015,2) + round(self.wynagrodzenie_brutto*0.0245,2)
        self.ubez = round((self.wynagrodzenie_brutto - self.skladka)*0.09,2)
        self.podatek = round((round((round(self.wynagrodzenie_brutto-111.25 - self.skladka,2))*0.18,2)-46.33) - round((round(self.wynagrodzenie_brutto-self.skladka,2))*0.0775,2),0)
        self.wyplata = round(self.wynagrodzenie_brutto - self.skladka - self.ubez - self.podatek,2)
        self.k_praco = round(self.wynagrodzenie_brutto*0.0976,2) + round(self.wynagrodzenie_brutto*0.065,2) + round(self.wynagrodzenie_brutto*0.0193,2) + round(self.wynagrodzenie_brutto*0.0245,2) + round(self.wynagrodzenie_brutto*0.001,2)

    def __repr__(self):
        return f"{self.imie} {self.wyplata:.2f} {self.k_praco:.2f} {self.wynagrodzenie_brutto+self.k_praco:.2f}"
    
    def koszt_ostateczny(self):
        return self.wynagrodzenie_brutto + self.k_praco

w_data = []
koszt = 0

for pracownik in range(liczba_pracownikow):
    dane_wejscowe = input()
    w_data.append(dane_wejscowe)

for dane in w_data:
    imie = dane.split(' ')[0]
    wynagrodzenie_all = int(dane.split(' ')[1])
    pracownik = Worker(imie,wynagrodzenie_all)
    print(pracownik)
    koszt += pracownik.koszt_ostateczny()

print(f"{koszt:.2f}")