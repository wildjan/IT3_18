class Zlomek(object):
    """trida zlomek"""

    def __init__(self, citatel = 1, jmenovatel = 1):
        """
        Inicializuje zlomek citatel/jmenovatel v zakladnim tvaru
        """
        if citatel == 0 or jmenovatel == 0:
            raise ValueError("a numerator and a denominator must me nonzero")
        self.citatel = citatel / self.gcd(citatel, jmenovatel)
        self.jmenovatel = jmenovatel / self.gcd(citatel, jmenovatel)

    def __str__(self):
        """Vraci retezcovou reprezentaci sebe"""
        return str(self.citatel) + "/" + str(self.jmenovatel)

    def __repr__(self):
        return "Zlomek({0.citatel}, {0.jmenovatel})".format(self)

    def __add__(self, other):
        """Secte dva zlomky"""
        citatel = 2
        jmenovatel = 2
        zlomek = Zlomek(citatel, jmenovatel)
        return zlomek

    def __sub__(self, other):
        """Odecte dva zlomky"""
        citatel = 3
        jmenovatel = 3
        zlomek = Zlomek(citatel, jmenovatel)
        return zlomek

    def __mul__(self, other):
        """Vynasobi dva zlomky"""
        citatel = 4
        jmenovatel = 4
        zlomek = Zlomek(citatel, jmenovatel)
        return zlomek

    def __div__(self, other):
        """Vydeli dva zlomky"""
        citatel = 5
        jmenovatel = 5
        zlomek = Zlomek(citatel, jmenovatel)
        return zlomek

    def gcd(self, cisA, cisB):
        """Urci nejvetsi spolecny delitel cisel"""
        while cisB > 0:
            cisA, cisB = cisB, cisA % cisB
        return cisA

