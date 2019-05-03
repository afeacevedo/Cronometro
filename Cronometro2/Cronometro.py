from Hora import *
from Minuto import *
from Segundo import *
from Decima import *

class Cronometro():
    def __init__(self):
        self.h = Hora()
        self.m = Minuto()
        self.s = Segundo()
        self.d = Decima()

    def avanzar(self):
        self.d.avanzar()
        if self.d.getValor() == 0:
            self.s.avanzar()
            if self.s.getValor() == 0:
                self.m.avanzar()
                if self.m.getValor() == 0:
                    self.h.avanzar()

    def getTiempo (self):
        return "{:02d}".format(self.h.getValor())+":"+"{:02d}".format(self.m.getValor())+":"+"{:02d}".format(self.s.getValor())+":"+"{:02d}".format(self.d.getValor())


    def retroceder(self):
        self.d.retroceder()
        if self.d.getValor() == self.d.getTope():
            self.s.retroceder()
            if self.s.getValor() == self.s.getTope():
                self.m.retroceder()
                if self.m.getValor() == self.m.getTope():
                    self.h.retroceder()

    def setTiempo(self, x):
        entero = []
        Lista = x.split(":")
        [entero.append(int(y)) for y in Lista]
        self.h.setValor(entero[0])
        self.m.setValor(entero[1])
        self.s.setValor(entero[2])
        self.d.setValor(entero[3])

 
                
