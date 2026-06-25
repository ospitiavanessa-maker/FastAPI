from pydantic import BaseModel


#crear modelo trasaccional
class TransaccionBase(BaseModel):
    cantidad: int
    vr_unitario: float
    factura_id: int


class TransaccionCrear(TransaccionBase):
    pass


class TransaccionEditar(TransaccionBase):
    pass

class Transaccion(TransaccionBase):
    id: int | None = None