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

    def setParteAlfabeticaDni(self, parteAlfabeticaDni):
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
        self.setParteNumericaDni(self.getDni()[:-1])
        self.setParteAlfabeticaDni(self.getDni()[-1])

    def checkLetra(self):
        return self._sanearNumero() and TablaAsignacion.calcularLetra(
            TablaAsignacion(), self.getParteNumericaDni()
        ) == self.getParteAlfabeticaDni()

    def checkLongitud(self):
        return len(self.getParteNumericaDni()) == self.LONGITUD_NUMEROS_DNI

    def checkCIF(self):
        return (
            self._sanearNumero() and self.checkLetra() and self.checkLongitud()
        )

    def checkDni(self):
        return (
            self._sanearNumero() and self.checkLetra() and self.checkLongitud()
        )

    def _sanearNumero(self):
        self._separarDni()
        return self.getParteNumericaDni().isnumeric()

    def obtenerLetra(self):
        return str(self.getParteAlfabeticaDni()) if self.checkDni() else None

    def __repr__(self):
        return ''.join(self.getDni())
