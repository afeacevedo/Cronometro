# creamos otro archivo clase llamado hora que hereda de UnidadTiempo

from UnidadTiempo import *

class Hora(UnidadTiempo):
    def __init__(self):
        self.valor = 0
        self.tope = 23
