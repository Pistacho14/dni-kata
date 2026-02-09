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
