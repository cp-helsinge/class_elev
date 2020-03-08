# Dette er hovedfilen som instuktørerne kan proppe indhold i
# Elever skal holde sig uden for denne fil

import datetime

class Menneske:
    ''' Dette er vores Menneske klasse '''
    def __init__ (self, fn, en):
        self.fornavn=fn
        self.efternavn=en
        self.arme=2
        self.ben=2
        self.fødtDato=0
        self.fødtMåned=0
        self.fødtÅr=0
        self.alder=None

    def printname(self):
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


jesper=Underviser()
print(jesper.arme)

