from src.tablaAsignacion import TablaAsignacion

class Dni:
    
    LONGITUD_NUMEROS_DNI = 8
    
    def __init__(self):
        self.dni = ''
        self.numeroSano = 0
        self.letraSana = ''

    def getDni(self):
        return self.dni
    
    def setDni(self, dni):
        self.dni = dni

    def getNumeroSano(self):
        return self.numeroSano
    
    def setNumeroSano(self, numeroSano):
        self.numeroSano = numeroSano
    
    def getLetraSana(self):
        return self.letraSana
    
    def setLetraSana(self, letraSana):
        self.letraSana = letraSana
    
    def _sanearNumero(self):
        Dni.setNumeroSano(self, Dni.getDni(self)[:-1])
        
    def _sanearLetra(self):
        Dni.setLetraSana(self, Dni.getDni(self)[-1])
        
    def _checkLetra(self):
        Dni._sanearLetra(self)
        Dni._sanearNumero(self)
        return TablaAsignacion.calcularLetra(TablaAsignacion(), Dni.getNumeroSano(self))
    
    def _checkLongitud(self):
        return len(Dni.getNumeroSano(self)) == Dni.LONGITUD_NUMEROS_DNI
    
    def checkCIF(self):
        return Dni._checkLetra(self) and Dni._checkLongitud(self)