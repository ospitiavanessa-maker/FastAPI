from fastapi import FastAPI, HTTPException, status 
from modelos.clientes import Cliente, ClienteCrear, ClienteEditar
from modelos.facturas import Factura, FacturaCrear, FacturaEditar
from modelos.transacciones import Transaccion, TransaccionCrear, TransaccionEditar

app = FastAPI()


lista_clientes:list[Cliente] = []
lista_facturas: list[Factura] = []
lista_transacciones: list[Transaccion] = []


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
    raise HTTPException(
        status_code=400, detail=f"El cliente con id {cliente_id}, no existe."
                        )  


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


@app.get("/facturas/{factura_id}", response_model=Factura)
async def listar_factura(factura_id: int):
    #recorrer la lista facturas
    for i, obj_factura in enumerate (lista_facturas):
        if obj_factura.id == factura_id:
            return obj_factura
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"La factura con id {factura_id}, no existe."
                        )            


# Ejemplo de la lógica utilizada para crear la factura
@app.post("/facturas/")
async def crear_factura(datos_factura: FacturaCrear):
    # Buscar cliente
    cliente_encontrado = None
    for cliente in lista_clientes:
        if cliente.id == datos_factura.cliente.id:
            cliente_encontrado = cliente
            break
    
    # Validar que el cliente exista
    if not cliente_encontrado:
        raise HTTPException(
            status_code=400, 
            detail=f"El cliente con ID {datos_factura.cliente_id} no existe"
        )
    
    # Transformar y validar datos
    factura_validada = Factura.model_validate(datos_factura.model_dump())
    
    # Asignar datos automáticos
    factura_validada.cliente = cliente_encontrado
    factura_validada.id = len(lista_facturas) + 1
    
    lista_facturas.append(factura_validada)
    return factura_validada


@app.patch("/facturas/{id_factura}", response_model=Factura)
async def editar_factura(id_factura: int, datos_factura: Factura):
    pass


@app.delete("/facturas/{id_factura}", response_model=Factura)
async def eliminar_factura (id_factura):
    pass


# |||||||||||||||||||||||||||||||
# crear los endpoint para transacciones


@app.get("/transacciones", response_model=list[Transaccion])
async def listar_transacciones():
    return lista_transacciones


@app.get("/transacciones/{id_transaccion}", response_model=Transaccion)
async def listar_transaccion(id_transaccion: int):
    for transaccion in lista_transacciones:
        if transaccion.id == id_transaccion:
            return transaccion
    raise HTTPException(
        status_code=400, detail=f"La transacción con id {id_transaccion}, no existe."
    )


@app.post("/transacciones/{id_factura}", response_model=Transaccion)
async def crear_transaccion(id_factura: int, datos_transaccion: Transaccion):
    # Buscar factura
    factura_encontrada = None
    for factura in lista_facturas:
        if factura.id == id_factura:
            factura_encontrada = factura
            break

    # Validar que la factura exista
    if not factura_encontrada:
        raise HTTPException(
            status_code=400,
            detail=f"La factura con ID {id_factura} no existe"
        )

    # Transformar y validar datos
    transaccion_validada = Transaccion.model_validate(datos_transaccion.model_dump())

    # Asignar datos automáticos
    transaccion_validada.factura_id = id_factura
    transaccion_validada.id = len(lista_transacciones) + 1

    lista_transacciones.append(transaccion_validada)
    return transaccion_validada


@app.patch("/transacciones/{id_transaccion}", response_model=Transaccion)
async def editar_transaccion(id_transaccion: int, datos_transaccion: Transaccion):
    pass


@app.delete("/transacciones/{id_transaccion}", response_model=Transaccion)
async def eliminar_transaccion(id_transaccion: int):
    pass