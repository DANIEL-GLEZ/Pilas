class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

    def esta_vacia(self):
        return len(self.items) == 0

    def ver_cima(self):
        if not self.esta_vacia():
            return self.items[-1]
        return None

def mover_discos(n, origen, destino, auxiliar):
    if n == 1:
        disco = origen.desapilar()
        destino.apilar(disco)
        print(f"Mueve el disco {disco} desde {origen.nombre} hasta {destino.nombre}")
    else:
        mover_discos(n-1, origen, auxiliar, destino)
        mover_discos(1, origen, destino, auxiliar)
        mover_discos(n-1, auxiliar, destino, origen)

torre1 = Pila()
torre1.nombre = "Origen"
torre2 = Pila()
torre2.nombre = "Destino"
torre3 = Pila()
torre3.nombre = "Auxiliar"

for disco in [3, 2, 1]:
    torre1.apilar(disco)

mover_discos(3, torre1, torre2, torre3)
