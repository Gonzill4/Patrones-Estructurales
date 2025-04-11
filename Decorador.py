# Gonzalo Calderon Gil Leyva | A01740008 | Decorador de Café
# Patrón Decorador: Permite añadir funcionalidad a un objeto de forma dinámica.


class Cafe:
    def descripcion(self):
        return "Café"

    def precio(self):
        return 2.0


# Decorador base
class CafeDecorador:
    def __init__(self, cafe):
        self._cafe = cafe

    def descripcion(self):
        return self._cafe.descripcion()

    def precio(self):
        return self._cafe.precio()


# Decoradores concretos
class Leche(CafeDecorador):
    def descripcion(self):
        return self._cafe.descripcion() + " + Leche"

    def precio(self):
        return self._cafe.precio() + 0.5


class Chocolate(CafeDecorador):
    def descripcion(self):
        return self._cafe.descripcion() + " + Chocolate"

    def precio(self):
        return self._cafe.precio() + 0.75


class Canela(CafeDecorador):
    def descripcion(self):
        return self._cafe.descripcion() + " + Canela"

    def precio(self):
        return self._cafe.precio() + 1.0


# Ejemplo 
pedido = Cafe()
pedido = Leche(pedido)
pedido = Canela(pedido)

print("Pedido:", pedido.descripcion())
print("Precio: $", pedido.precio())