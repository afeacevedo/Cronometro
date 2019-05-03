# creamos otro archivo clase llamado decimas que hereda de UnidadTiempo

from UnidadTiempo import *

class Decima(UnidadTiempo):
    def __init__(self):
        self.valor = 0
        self.tope = 9
