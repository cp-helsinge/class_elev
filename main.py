# Dette er hovedfilen som instuktørerne kan proppe indhold i
# Elever skal holde sig uden for denne fil

import datetime

class Menneske:
    ''' Dette er vores Menneske klasse '''
    def __init__ (self):
        self.fornavn=None
        self.efternavn=None
        self.arme=2
        self.ben=2
        self.fødtDag=0
        self.fødtMåned=0
        self.fødtÅr=0

    def fuldeNavn(self):
        print(self.fornavn, self.efternavn)

    def antalArme(self):
        print("Jeg har",arme,"arme")
        return self.arme

    def antalBen(self):
        print("Jeg har",ben,"ben")
        return self.ben

    def hvorGammel(self):
        print("Jeg er",alder,"år gammel")
        return self.alder

    def alder(self):
        nu = date.today()
        fdag = date(self.fødtÅr, self.fødtMåned, self.fødtDag)
        return nu.year - fdag.year - ((nu.month, day) < (fdag.month, fDag.day))


class Elev(Menneske):
    ''' Dette er vores Elev klasse som nedarver fra Menneske klassen '''
    def __init__ (self):
        super().__init__()
        self.uartig="Nej"

    def erUartig(self):
        return self.uartig


class Underviser(Menneske):
    ''' Dette er vores Underviser klasse som nedarver fra Menneske klassen '''
    def __init__ (self):
        super().__init__()
        self.streng="Ja"

    def erStreng(self):
        return self.streng

obj=Underviser()
obj.fornavn="Jesper"
obj.efternavn="Sommer"
obj.fødtDato=27
obj.fødtMåned=3
obj.fødtÅr=1973
print(obj.antalArme)
print(obj.fuldeNavn,"har",obj.arme,"arme,",obj.ben,"ben, og er",obj.alder,"år gammel")
