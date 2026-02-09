from src.tablaAsignacion import TablaAsignacion


class Dni:
    LONGITUD_NUMEROS_DNI = 8

    def __init__(self):
        self.dni = ""
        self.numeroDni = ""
        self.letraDni = ""
        self.numeroSano = False
        self.letraSana = False

    def getDni(self):
        return self.dni

    def setDni(self, dni):
        self.dni = dni

    def getNumeroDni(self):
        return self.numeroDni

    def setNumeroDni(self, numeroDni):
        self.numeroDni = numeroDni

    def getLetraDni(self):
        return self.letraDni

    def setLetraDni(self, letraDni):
        self.letraDni = letraDni

    def getNumeroSano(self):
        return self.numeroSano
    
    def setNumeroSano(self, numeroSano):
        self.numeroSano = numeroSano
    
    def getLetraSana(self):
        return self.letraSana
    
    def setLetraSana(self, letraSana):
        self.letraSana = letraSana
    
    def _separarDni(self):
        Dni.setNumeroDni(self, Dni.getDni(self)[:-1])
        Dni.setLetraDni(self, Dni.getDni(self)[-1])

    def _checkLetra(self):
        Dni._separarDni(self)
        return TablaAsignacion.calcularLetra(TablaAsignacion(), Dni.getNumeroDni(self)) == Dni.getLetraDni(self)

    def _checkLongitud(self):
        return len(Dni.getNumeroDni(self)) == Dni.LONGITUD_NUMEROS_DNI

    def checkCIF(self):
        return Dni._sanearNumero(self) and Dni._checkLetra(self) and Dni._checkLongitud(self)
    
    def checkDni(self):
        return Dni._sanearNumero(self) and Dni._checkLetra(self) and Dni._checkLongitud(self)
    
    def _sanearNumero(self):
        Dni._separarDni(self)
        return Dni.getNumeroDni(self).isnumeric()
