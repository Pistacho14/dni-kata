from src.tablaAsignacion import TablaAsignacion


class Dni:
    LONGITUD_NUMEROS_DNI = 8

    def __init__(self):
        self.dni = ""
        self.parteNumericaDni = ""
        self.parteAlfabeticaDni = ""
        self.numeroSano = False
        self.letraSana = False

    def getDni(self):
        return self.dni

    def setDni(self, dni):
        self.dni = dni

    def getParteNumericaDni(self):
        return self.parteNumericaDni

    def setParteNumericaDni(self, parteNumericaDni):
        self.parteNumericaDni = parteNumericaDni

    def getParteAlfabeticaDni(self):
        return self.parteAlfabeticaDni

    def setparteAlfabeticaDni(self, parteAlfabeticaDni):
        self.parteAlfabeticaDni = parteAlfabeticaDni

    def getNumeroSano(self):
        return self.numeroSano

    def setNumeroSano(self, numeroSano):
        self.numeroSano = numeroSano

    def getLetraSana(self):
        return self.letraSana

    def setLetraSana(self, letraSana):
        self.letraSana = letraSana

    def _separarDni(self):
        Dni.setParteNumericaDni(self, Dni.getDni(self)[:-1])
        Dni.setparteAlfabeticaDni(self, Dni.getDni(self)[-1])

    def checkLetra(self):
        Dni._separarDni(self)
        return Dni._sanearNumero(self) and TablaAsignacion.calcularLetra(
            TablaAsignacion(), Dni.getParteNumericaDni(self)
        ) == Dni.getParteAlfabeticaDni(self)

    def checkLongitud(self):
        return len(Dni.getParteNumericaDni(self)) == Dni.LONGITUD_NUMEROS_DNI

    def checkCIF(self):
        return (
            Dni._sanearNumero(self) and Dni.checkLetra(self) and Dni.checkLongitud(self)
        )

    def checkDni(self):
        return (
            Dni._sanearNumero(self) and Dni.checkLetra(self) and Dni.checkLongitud(self)
        )

    def _sanearNumero(self):
        Dni._separarDni(self)
        return Dni.getParteNumericaDni(self).isnumeric()

    def obtenerLetra(self):
        return str(Dni.getParteAlfabeticaDni(self)) if Dni.checkDni(self) else None

    def __repr__(self):
        return Dni.getDni(self)
