class Cislo(object):
    """trida cislo"""

    def __init__(self, cislo = 0):
        """
        Inicializuje cislo
        """

        # TODO: 1. doplnte kod pro inicializaci
        self.cislo = None

    def __str__(self):
        """Vraci cislo jako retezec"""

        # TODO: 2. doplnte kod pro string metodu
        return "0"

    def __repr__(self):
        """Vraci reprezentaci sebe sama"""
        return "Cislo({0.cislo})".format(self)

    def __add__(self, other):
        """Secte dve cisla. Vraci objekt Cislo!"""

        # TODO: 3. Napiste kod pro magickou metodu soucet
        soucet = None
        return None

    def __sub__(self, other):
        """Odecte dve cisla. Vraci objekt Cislo!"""

        # TODO: 4. Napiste kod pro magickou metodu rozdil
        rozdil = None 
        return None

    def __mul__(self, other):
        """Vynasobi dve cisla. Vraci objekt Cislo!"""

        # TODO: 5. Napiste kod pro magickou metodu soucin
        soucin = None
        return None

    def __div__(self, other):
        """Vydeli dve cisla. Vraci objekt Cislo!"""

        # TODO: 6. Napiste kod pro magickou metodu podil
        podil = None
        return None

    # TODO: 7. CHALENGE- napiste kod pro magickou metodu umocnovani
