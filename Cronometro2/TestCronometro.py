from Cronometro import *

c = Cronometro()
x = "01:20:30:02"

c.setTiempo(x)
for i in range(1000):
    c.retroceder()
    print c.getTiempo()
