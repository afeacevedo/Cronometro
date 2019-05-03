class UnidadTiempo():
    def __init__(self):
        self.valor = 0
        self.tope = 0

# el objeto puede avanzar hasta que sea menor que el valor del tope
    def avanzar(self):
        if self.valor < self.tope:
            self.valor += 1  # self.valor = self.valor+1
        else:
            self.valor = 0

    def getValor(self):
        return self.valor
        

    def setValor(self, v):
        self.valor = v
    
    def getTope(self):
        return self.tope
    
    def retroceder(self):
        if self.valor > 0:
            self.valor -= 1
        else:
            self.valor = self.tope
        
