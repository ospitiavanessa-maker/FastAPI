from pydantic import BaseModel
from .clientes import Cliente

#proviene de python y sirve para convertir un metodo de una clase en una propiedad de solo lectura.
#, @computed_field es un decorador que te permite definir propiedades o metodos que se calculan dinamicamente
# nativa de python.


#cciones(id, fecha, vr_total, clientes)
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