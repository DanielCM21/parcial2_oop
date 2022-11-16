from abc import ABC, abstracmethod
class Parqueadero(ABC):
    def __init__(self, usuario, plazas_disponibles) -> None:
        self.usuario = usuario
        self.plazas_disponibles = plazas_disponibles

    def registro():
        pass
    
    @abstracmethod
    def reserva():
        pass

class Coches:
    def __init__(self, cantidad_vehiculos) -> None:
        self.cantidad_vehiculos = cantidad_vehiculos

    @property
    def tipo_vehiculo():
        pass
    
class Horario:

    @property
    def tiempodeparqueo():
        pass

class Cobro:
    
    def precioapagar():
        pass
