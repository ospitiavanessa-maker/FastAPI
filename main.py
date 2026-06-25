from fastapi import FastAPI, HTTPException
from modelos.clientes import Cliente, ClienteCrear, ClienteEditar
from modelos.facturas import Factura
from modelos.transacciones import Transaccion

app = FastAPI()


lista_clientes:list[Cliente] = []
lista_facturas: list[Factura] = []
lista_transacciones: list[Transacciones] = []


#endpoint, para obtener o listar todos los clientes
@app.get("/clientes")
async def listar_clientes():
    return lista_clientes


#endpoint, para obtener o listar un solo cliente de la lista
@app.get("/clientes/{cliente_id}")
async def listar_cliente(cliente_id: int):
    #recorrer la lista clientes
    for i, obj_cliente in enumerate (lista_clientes):
        if obj_cliente.id == cliente_id:
            return obj_cliente


#endpoint, para crear un cliente, y agregar a la lista
@app.post("/clientes", response_model=Cliente)
async def crear_cliente(datos_cliente: ClienteCrear): 
    cliente_val = Cliente.model_validate(datos_cliente.model_dump())

    id_cliente = len(lista_clientes)+1
    cliente_val.id = id_cliente
    lista_clientes.append (cliente_val)
    return cliente_val


#endpoint, para editar un cliente, y agregar a la lista
@app.patch("/clientes", response_model=Cliente)
async def editar_cliente(cliente_id: int, datos_cliente: ClienteEditar):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            #validar cliente
            cliente_val = Cliente.model_validate(datos_cliente.model_dump())
            cliente_val.id = cliente_id
            lista_clientes[i] = cliente_val
            return cliente_val
    raise HTTPException(
        status_code=400,detail=f"El cliente con id {cliente_id}, no existe."
    )


#endpoint, para eliminar un cliente
@app.delete("/clientes/{cliente_id}")
async def eliminar_cliente(cliente_id: int):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            lista_clientes.pop(i)
            return {"mensaje": f"Cliente con id {cliente_id} eliminado correctamente."}
    raise HTTPException(
        status_code=400, detail=f"El cliente con id {cliente_id}, no existe."
    )


# |||||||||||||||||||||||||||||||
#Crear los enpoint para facturas


@app.get("/facturas", response_model=list[Factura])
async def listar_facturas():
    return lista_facturas


@app.get("/facturas/{id_factura}", response_model=Factura)
async def listar_factura(id_factura: int):
    pass


@app.post("/facturas/{id_cliente}", response_model=Factura)
async def crear_factura(id_cliente: int, datos_factura: Factura):
    pass


@app.patch("/facturas/{id_factura}", response_model=Factura)
async def editar_factura(id_factura: int, datos_factura: Factura):
    pass


@app.delate("/facturas/{id_factura}", response_model=Factura)
async def eliminar_factura (id_factura):
    pass


# |||||||||||||||||||||||||||||||
# crear los endpoint para transacciones


@app.get("/transacciones", response_model=list[Transaccion])
async def listar_ftransacciones():
    pass


@app.get("/transacciones/{id_transaccion}", response_model=Transaccion)
async def listar_transaccion(id_transaccion: int):
    pass


@app.post("/transacciones/{id_factura}", response_model=Transaccion)
async def crear_transaccion(id_factura: int, datos_transaccion: Transaccion):
    pass


@app.patch("/transacciones/{id_transaccion}", response_model=Transaccion)
async def editar_transaccion(id_transaccion: int, datos_transaccion: Transaccion):
    pass


@app.delete("/transacciones/{id_transaccion}", response_model=Transaccion)
async def eliminar_transaccion(id_transaccion: int):
    pass