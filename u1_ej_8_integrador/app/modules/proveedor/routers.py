from fastapi import APIRouter, HTTPException, status, Path, Query
from . import schemas, services

router = APIRouter(prefix="/proveedores", tags=["Proveedores"])

@router.post("/", response_model=schemas.ProveedorRead, status_code=status.HTTP_201_CREATED)
def alta_proveedor(proveedor: schemas.ProveedorCreate):
    try:
        return services.crear_proveedor(proveedor)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))

@router.get("/", response_model=list[schemas.ProveedorRead], status_code=status.HTTP_200_OK)
def listar_proveedores(skip: int = Query(0, ge=0), limit: int = Query(10, ge=1, le=50), activo: bool | None = None):
    return services.obtener_proveedores(skip, limit, activo)
    
@router.get("/{id}", response_model=schemas.ProveedorRead, status_code=status.HTTP_200_OK)
def obtener_proveedor(id: int= Path(..., ge = 1)):
    proveedor = services.obtener_por_id(id)

    if not proveedor:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail= "Proveedor no encontrado")
    return proveedor

@router.put("/{id}", response_model=schemas.ProveedorRead, status_code=status.HTTP_200_OK)
def actualizar_proveedor(proveedor: schemas.ProveedorCreate, id: int = Path(..., ge = 1)):

    try:
        proveedor_actualizado = services.actualizar_total(id, proveedor)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))

    if not proveedor_actualizado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Proveedor no encontrado")

    return proveedor_actualizado

@router.put("/{id}/desactivar", response_model=schemas.ProveedorRead, status_code=status.HTTP_200_OK)
def borrado_logico(id: int = Path(..., gt=0)):
    try:
        desactivado = services.desactivar(id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))

    if not desactivado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Proveedor no encontrado"
        )
    return desactivado