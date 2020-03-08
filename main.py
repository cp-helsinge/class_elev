# Dette er hovedfilen som instuktørerne kan proppe indhold i
# Elever skal holde sig uden for denne fil

class Menneske
    fornavn=""
    efternavn=""
    arme=2
    ben=2
    def antalArme(self): arme
    def antalBen(self): ben

class DerivedClass(Menneske): Elev
    uartig="Nej"
    def erUartig(self): uartig

class DerivedClass(Menneske): Underviser
    streng="Ja"
    def erStreng(self): uartig
