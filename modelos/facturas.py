from pydantic import BaseModel, computed_field
from datetime import datetime
from typing import List
from modelos.clientes import Cliente
from modelos.transacciones import Transaccion

#proviene de python y sirve para convertir un metodo de una clase en una propiedad de solo lectura.
#, @computed_field es un decorador que te permite definir propiedades o metodos que se calculan dinamicamente
# nativa de python.


#crear modelo trasacciones(id, fecha, vr_total, clientes)
class Factura(BaseModel):
    id: int = None
    fecha: datetime = datetime.now()
    cliente: Cliente
    transacciones: List[Transaccion] = []

    @property
    def valor_total(self) -> float:
        # Lógica para calcular el total
        return 222.0  # Valor de prueba utilizado en el video

    @computed_field
    def total(self) -> float:
        return self.valor_total


class FacturaBase(BaseModel):
    fecha: str
    vr_total: float 
    cliente: Cliente


class FacturaCrear(FacturaBase):
    pass


class FacturaEditar(FacturaBase):
    pass


class Factura(FacturaBase):
    id: int | None = None