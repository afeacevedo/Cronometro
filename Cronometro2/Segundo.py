# creamos otro archivo clase llamado minuto que hereda de UnidadTiempo. 
# cambia con respecto a hora que va hasta 59

from UnidadTiempo import *

class Segundo(UnidadTiempo):
    def __init__(self):
        self.valor = 0
        self.tope = 59
