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
    def tipo_vehiculo(self):
        return self.tipo_vehiculo
    
    @tipo_vehiculo.setter
    def tipo_vehiculo(self, tipo):
        if tipo != "SUV" or "Compacto" or "VAN":
            print("Es correcto el tipo te vehiculo ingresado")
        else:
            print("No es un vehiculo disponible")
class Horario:

    @property
    def tiempodeparqueo(self):
        pass

class Cobro:
    
    def precioapagar():
        pass
