# Dette er hovedfilen som instuktørerne kan proppe indhold i
# Elever skal holde sig uden for denne fil

class Menneske:
    ''' Dette er vores Menneske klasse '''
    def __init__ (self)
        fornavn=""
        efternavn=""
        arme=2
        ben=2

    def antalArme(self):
        print("Jeg har",arme,"arme")
        return self.arme

    def antalBen(self):
        print("Jeg har",ben,"ben")
        return self.ben


class DerivedClass(Menneske): Elev
    ''' Dette er vores Elev klasse som nedarver fra Menneske klassen '''
    def __init__ (self):
        uartig="Nej"

    def erUartig(self):
        return self.uartig


class DerivedClass(Menneske): Underviser
    ''' Dette er vores Underviser klasse som nedarver fra Menneske klassen '''

    def __init__ (self):
        streng="Ja"

    def erStreng(self):
        return self.streng



