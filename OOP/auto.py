
class Auto:
    def __init__(self, model, jahr, farbe, preis):
        self.model = model
        self.jahr = jahr 
        self.farbe = farbe 
        self.preis = preis

    def fahren(self):
        print(f"Du fährst den {self.farbe}en {self.model}")

    def beschreiben(self):
        print(f"Das AUto ist ein {self.farbe}er {self.model} aus dem Jahr {self.jahr}")
