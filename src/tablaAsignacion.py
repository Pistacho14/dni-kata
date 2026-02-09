class TablaAsignacion:
    
    def __init__(self):
        self.tabla = (
            "T",
            "R",
            "W",
            "A",
            "G",
            "M",
            "Y",
            "F",
            "P",
            "D",
            "X",
            "B",
            "N",
            "J",
            "Z",
            "S",
            "Q",
            "V",
            "H",
            "L",
            "C",
            "K",
            "E",
        )
    
    def getTabla(self):
        return self.tabla
    
    def getLetra(self, posicion):
        try:
            return self.tabla[posicion]
        except IndexError:
            return "Posicion letra fuera de rango"

    def calcularLetra(self, cifras):
        return TablaAsignacion.getTabla(self)[int(cifras) % len(TablaAsignacion.getTabla(self))]
    
    def getModulo(self):
        return (len(TablaAsignacion.getTabla(self)))
    
    def isLetraPermitida(self, letra):
        return letra in TablaAsignacion.getTabla(self)
    

    def __repr__(self):
        return "Tabla de asignación"
