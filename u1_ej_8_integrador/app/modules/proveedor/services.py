from .schemas import ProveedorRead, ProveedorCreate

db_proveedores:list[ProveedorRead] = []
id_counter = 1

def crear_proveedor(data: ProveedorCreate) -> ProveedorRead:

    for p in db_proveedores:
        if p.codigo == data.codigo:
            raise ValueError("El código del proveedor ya existe")

    global id_counter
    nuevo = ProveedorRead(id = id_counter, **data.model_dump())
    id_counter+= 1
    db_proveedores.append(nuevo)
    return nuevo

def obtener_proveedores(skip: int, limit: int, activo: bool | None = None) -> list[ProveedorRead]:
    proveedores = db_proveedores

    if activo is not None:
        proveedores = [p for p in proveedores if p.activo == activo]
        
    return proveedores[skip: skip + limit]

def obtener_por_id(id:int) -> ProveedorRead | None:
    for p in db_proveedores:
       if p.id == id:
           return p
    return None

def actualizar_total(id:int, data: ProveedorCreate) -> ProveedorRead | None:
    for p in db_proveedores:
        if p.id != id and p.codigo == data.codigo:
            raise ValueError("El código del proveedor ya existe.")

    for index, p in enumerate(db_proveedores):
            if p.id == id:
                proveedor_actualizado = ProveedorRead(id=id, **data.model_dump())
                db_proveedores[index] = proveedor_actualizado
                return proveedor_actualizado
    return None

def desactivar(id: int) -> ProveedorRead | None:
    
    for index, p in enumerate(db_proveedores):
        if p.id == id:

            if not p.activo:
                raise ValueError("El proveedor ya se encuentra desactivado.")
            
            p_dict = p.model_dump()
            p_dict["activo"] = False
            proveedor_actualizado = ProveedorRead(**p_dict)
            db_proveedores[index] = proveedor_actualizado
            return proveedor_actualizado
    return None

