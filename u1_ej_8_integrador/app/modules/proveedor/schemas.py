from pydantic import BaseModel, Field

class ProveedorBase(BaseModel):
    codigo: str = Field(..., min_length=1)
    razon_social: str = Field(min_length=3)
    cuit: str = Field(min_length=11, max_length=15)
    email: str = ""
    telefono: str = ""
    activo: bool = True

class ProveedorCreate(ProveedorBase):
    pass

class ProveedorRead(ProveedorBase):
    id: int

class ProveedorUpdate(ProveedorBase):
    codigo: str | None = Field(None ,min_length=1)
    razon_social: str | None = Field(None, min_length=3)
    cuit: str | None = Field(None, min_length=11, max_length=15)
    email: str | None = None
    telefono: str | None = None
    activo: bool | None = True 

